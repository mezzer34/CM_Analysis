import sys
sys.setrecursionlimit(2000)

print("Python version: " + sys.version)




import matplotlib.pyplot as plt



import file_func as file_func
import functions as f
import grapthing as grapth
import dataprocessing as processing
import emailfunc as em

import structs as st       
    
    

    
def main():    
    
    #loop and get user options until they quit    
    l_ValidUserOptions = ["1", "2", "8", "9", "q"]
    
    l_MasterModel = st.Model()
        
    while True:

        
        doPrintCurrentStatus(_CurrentModel=l_MasterModel)
        doPrintUserModeOptions()
        l_OperatingMode_UserSelection = getUserOperatingMode(l_ValidUserOptions)
        
        

        if l_OperatingMode_UserSelection == "1":
            print("Loading existing model...")
            
            l_MasterModel = doOperatingMode_LoadExistingModel()

        elif l_OperatingMode_UserSelection == "2":
            print("Loading from CSV to compare against existing model...")
            
            doOperatingMode_CheckAgainstModel(_ComparrisonDataset=l_MasterModel)

        elif l_OperatingMode_UserSelection == "8":
            print("Downloading files from email server") 
            
            doDownloadEmails()
            

        elif l_OperatingMode_UserSelection == "9":
            print("Loading from CSV and generating reference Model...") 
            
            l_MasterModel = doOperatingMode_LearnDataset()
            
        elif l_OperatingMode_UserSelection == "q":
            print("Exiting")
            print("")
            
            exit()





def doOperatingMode_LoadExistingModel():
    #Let user select which dataset to load
    l_UserFileNameSelection = file_func.doGetFileNameSelectionFromUser(_MaxNumberOfFilesToSelect=1, 
                                                                       _DirectoryPath="./LearnedData/")
    
    
    #Load the model from file
    l_LoadedModel = file_func.doLoadModelFromFile(_FullFilepath=l_UserFileNameSelection[0])
    
    return l_LoadedModel
    




def doOperatingMode_CheckAgainstModel(_ComparrisonDataset: st.Model):    
    l_Models = processing.doLoadFromCSVAndConvertToModel(_DirectoryPath="./data/",
                                                         _MaxNumberOfFilesToSelect = 0)
    
    #print comparison between two models
    for i in range(len(l_Models)):
        grapth.doPlotModel(_MasterModel=_ComparrisonDataset,
                           _OtherModel=l_Models[i],
                           _ChartType=st.ChartType.Lineplot,
                           _PlotData=st.PlotData.MasterOther_Compare_All_WithDiff)
        
       
        l_TimeExceededList = doFindAmountOfTimeVibrationWasAboveLimits(_MasterModel=_ComparrisonDataset,
                                                                      _OtherModel=l_Models[i])
       
        #print the amount of time the vibration was above the limits
        if l_TimeExceededList[0] == 0:
            print("X Axis Ok")

        else:
            print("X Axis Failed - "+ str(l_TimeExceededList[0]) + " seconds")

        if l_TimeExceededList[1] == 0:
            print("Y Axis Ok")

        else:
            print("Y Axis Failed - "+ str(l_TimeExceededList[1]) + " seconds")

        if l_TimeExceededList[2] == 0:
            print("Z Axis Ok")

        else:
            print("Z Axis Failed - "+ str(l_TimeExceededList[2]) + " seconds")


        print("")
        print("")       
       
       
       
    plt.show()
    
    input("Pess enter to continue")




def doOperatingMode_LearnDataset():   
    l_NewModelList = processing.doLoadFromCSVAndConvertToModel(_DirectoryPath="./data/",
                                                               _MaxNumberOfFilesToSelect = 1)
    
    l_NewModel = st.Model()
    l_NewModel = l_NewModelList[0]
    
    #get new dataset name
    print("Motor name from file: " + l_NewModel.Name)
    l_NewName = f.getUserInput("Enter new Motor Dataset name: ", _AllowBlank=True)
    
    if l_NewName != "":
        #set the name of the model
        l_NewModel.Name = l_NewName
    
    if l_NewModel.Name == "":
        l_NewModel.Name = "New Model"
        



    #save the new model to file
    file_func.doSaveModelToFile(_DataToStore=l_NewModel, 
                                _FullFilepath= "./LearnedData/" + l_NewModel.Name)


    
    return l_NewModel


def doDownloadEmails():
    
    l_Result = em.doGetMail()

    
    print(l_Result)



def doPrintCurrentStatus(_CurrentModel: st.Model):
    
    
    #if there is data in the current model display it, otherwise display warning    
    if ( (len(_CurrentModel.Name) > 0) and ( _CurrentModel.ModelLoaded ) ):        
        doPrintModelToScreen(_Model=_CurrentModel)
                
    else:
        print("No model loaded")
        
    
    
    print("Waiting for user input")
    print("\n")
    

def doPrintModelToScreen(_Model: st.Model):
    print("Model Name: " + _Model.Name)
    print("Model Date: " + _Model.OriginDate)
    print("")
    print("Model Data: ")
    
    
    l_VibrationAxis = st.VibrationData()
    l_VibrationAxis = _Model.VibrationLog
    doPrintAxisDataToScreen(_AxisData=l_VibrationAxis.XAxis)
    doPrintAxisDataToScreen(_AxisData=l_VibrationAxis.YAxis)
    doPrintAxisDataToScreen(_AxisData=l_VibrationAxis.ZAxis)
    
    print("")
    print("")
    
    



def doPrintAxisDataToScreen(_AxisData: st.VibrationAxis):
    print(" |")
    print(" |   Axis Name:  " + _AxisData.AxisName)
    print(" |")
    print(" |   Min:        ", _AxisData.Min)
    print(" |   Max:        ", _AxisData.Max)
    print(" |   Mean:       ", _AxisData.Mean)
    print(" |   Stand Dev:  ", _AxisData.StandDev)
    print(" |---------------------------------------------------")




def doPrintModelDifferences(_ModelDifferences: st.ModelDifference):
    print(" |---------------------------------------------------")
    print(" |   Master Model Name:   " + _ModelDifferences.MasterName)
    print(" |   Other Model Name:    " + _ModelDifferences.OtherName)
    print(" |---------------------------------------------------")
    
    doPrintAxisDifferences(_AxisDifferences=_ModelDifferences.XAxis, _AxisName="X")
    doPrintAxisDifferences(_AxisDifferences=_ModelDifferences.YAxis, _AxisName="Y")
    doPrintAxisDifferences(_AxisDifferences=_ModelDifferences.ZAxis, _AxisName="Z")
    
    print("")
    print("")
    
    print("")



def doPrintAxisDifferences(_AxisDifferences: st.AxisDifference, _AxisName: str):
    
    l_MinDiff = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.MinDiff,
                                           _Digits_BeforeDecimal = 3, 
                                           _Digits_AfterDecimal = 6)
    l_MinDiff_prnt = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.MinDiff,
                                                _Digits_BeforeDecimal = 2, 
                                                _Digits_AfterDecimal = 3)
    
    l_MaxDiff = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.MaxDiff, 
                                           _Digits_BeforeDecimal = 3, 
                                           _Digits_AfterDecimal = 6)
    l_MaxDiff_prnt = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.MaxDiff,
                                                _Digits_BeforeDecimal = 2, 
                                                _Digits_AfterDecimal = 3)
    
    l_MeanDiff = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.MeanDiff, 
                                            _Digits_BeforeDecimal = 3, 
                                            _Digits_AfterDecimal = 6)
    l_MeanDiff_prnt = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.MeanDiff,
                                                 _Digits_BeforeDecimal = 2, 
                                                 _Digits_AfterDecimal = 3)
    
    l_StandDevDiff = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.StandDevDiff, 
                                                _Digits_BeforeDecimal = 3, 
                                                _Digits_AfterDecimal = 6)
    l_StandDevDiff_prnt = f.doGetNumberOfFixedLength(_Number = _AxisDifferences.StandDevDiff,
                                                     _Digits_BeforeDecimal = 2, 
                                                     _Digits_AfterDecimal = 3)
    
    
    
    #print info
    print(" |   Axis Name:  " + _AxisName)
    print(" |")
    print(" |   Min Diff:       " + l_MinDiff + " (" + l_MinDiff_prnt + "%)")
    print(" |   Max Diff:       " + l_MaxDiff + " (" + l_MaxDiff_prnt + "%)")
    print(" |   Mean Diff:      " + l_MeanDiff + " (" + l_MeanDiff_prnt + "%)")
    print(" |   Stand Dev Diff: " + l_StandDevDiff + " (" + l_StandDevDiff_prnt + "%)")
    print(" |---------------------------------------------------")
    

    return False





def getUserOperatingMode(l_ValidOperations: list[str]):
    # loop to get user input
    while True:
        
        User_input = f.getUserInput("Enter selection: ", _AllowBlank=True)

        #check if the user input is valid
        if User_input in l_ValidOperations:
            return User_input
        
        else:
            print("Invalid input. Please try again.")




def doPrintUserModeOptions():
    print("Select operating mode")
    print("1 - Load existing model")
    print("2 - Load data from file and check against model")
    print("9 - Load data from file to learn model")
    print("q - Quit")
    print("")





def doFindAmountOfTimeVibrationWasAboveLimits(_MasterModel: st.Model, _OtherModel: st.Model):
    
    l_XAxis_FramesExceeded = doFindAmountOfFramesListExceedsMax(_ListToCheck=_OtherModel.VibrationLog.XAxis.RawData,
                                                                _MaxValue=_MasterModel.VibrationLog.XAxis.Max)
    
    l_YAxis_FramesExceeded = doFindAmountOfFramesListExceedsMax(_ListToCheck=_OtherModel.VibrationLog.YAxis.RawData,
                                                                _MaxValue=_MasterModel.VibrationLog.YAxis.Max)
    
    l_ZAxis_FramesExceeded = doFindAmountOfFramesListExceedsMax(_ListToCheck=_OtherModel.VibrationLog.ZAxis.RawData,
                                                                _MaxValue=_MasterModel.VibrationLog.ZAxis.Max)
    
    
    l_TimePerFrame = _MasterModel.VibrationLog.Time[1] - _MasterModel.VibrationLog.Time[0]
    
    l_XAxis_TimeExceeded = l_XAxis_FramesExceeded * l_TimePerFrame
    l_YAxis_TimeExceeded = l_YAxis_FramesExceeded * l_TimePerFrame
    l_ZAxis_TimeExceeded = l_ZAxis_FramesExceeded * l_TimePerFrame
    
    l_TimeEcceededList = [l_XAxis_TimeExceeded, l_YAxis_TimeExceeded, l_ZAxis_TimeExceeded]
    
    return l_TimeEcceededList
    
    
    
    

def doFindAmountOfFramesListExceedsMax(_ListToCheck: list[float], _MaxValue: float):
    
    l_AmountOfFramesExceedingMax = 0
    
    for i in range(0, len(_ListToCheck)):
        if (_ListToCheck[i] > _MaxValue):
            l_AmountOfFramesExceedingMax += 1
            
    return l_AmountOfFramesExceedingMax




if __name__ == "__main__":
    #print python version (Very jank, shush)
    version = sys.version_info
    
    #Who decided that python versions should be managed like this??? Its terrible
    
    if version.major == 3 and version.minor >= 9:
        main()
    
    else:
        raise Exception("Must be using Python 3.9")
