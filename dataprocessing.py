import functions as f
import structs as st

import file_func as file_func



def doLoadFromCSVAndConvertToModel(_DirectoryPath):
    l_UserFileNameSelection = file_func.doGetFileNameSelectionFromUser(_MaxNumberOfFilesToSelect=1, 
                                                                       _DirectoryPath=_DirectoryPath)


    #Get useable data from file name
    l_LoadedVibrationDataList = doLoadCSVAndStoreAsVibrationDataStruct(_UserFileNameSelection=l_UserFileNameSelection)
    
    
    #Convert list of vibration data to models
    l_NewModelsList = []    
    for l_Data in l_LoadedVibrationDataList:
        l_NewModelsList.append(doGenerateModelFromDataset(l_Data, "TestModel"))


    return l_NewModelsList



def doLoadCSVAndStoreAsVibrationDataStruct(_UserFileNameSelection):
    l_VibrationDataList = []
    for l_FileName in _UserFileNameSelection:        
        l_VibrationDataList.append(doLoadFileAndConvertToVibrationDataStruct(_FileToLoad=l_FileName, 
                                                                            subset_size=100))
        
    
    return l_VibrationDataList
    

    
    
def doLoadFileAndConvertToVibrationDataStruct(_FileToLoad, subset_size):

    # open files from user selection and load data
    l_LoadedLines = file_func.doLoadDataFromSelectedFile(_FileToLoad=_FileToLoad)
    
    l_LoadedLines = f.doTrimLines(lines=l_LoadedLines, 
                                    front_trim=3, 
                                    back_trim=0)
    


    Time, X, Y, Z = doGenerateRawVibrationDataLists(_LoadedLines=l_LoadedLines)

 
    
    #add the data to a vibration data object
    l_VibrationData = st.VibrationData()
    
    l_VibrationData.Time =Time
    
    l_VibrationData.XAxis = doAddDataToVibrationAxis(_DataToAdd=X, _AxisName="X")
    l_VibrationData.YAxis = doAddDataToVibrationAxis(_DataToAdd=Y, _AxisName="Y")
    l_VibrationData.ZAxis = doAddDataToVibrationAxis(_DataToAdd=Z, _AxisName="Z")
       
    
    return l_VibrationData


def doGenerateRawVibrationDataLists(_LoadedLines):
    Time = []
    X = []
    Y = []
    Z = []


    for n in range(len(_LoadedLines)):
        line = _LoadedLines[n]

        # remove new line from the end
        line = line.strip("\n")
        data_point = []

        data_point = line.split(",")
        Time.append((float(data_point[1]) / 1000))  # convert to seconds
        X.append(float(data_point[2]))
        Y.append(float(data_point[3]))
        Z.append(float(data_point[4]))
        
        
    return Time, X, Y, Z




def doGenerateModelFromDataset(_VibrationData, _ModelName):
    
    l_NewModel = st.Model()
    
    l_NewModel.Name = _ModelName
    
    
    #set origin date to now
    l_NewModel.OriginDate = f.getCurrentSystemDateTime()
    
    
    l_NewModel.VibrationData = _VibrationData
    
       
      
    return l_NewModel




    
def doCreateComparrisonBetweenTwoModels(_MasterModel, _OtherModel):
    #get the data from the model 
    
    l_ModelToSample = st.Model()    
    l_ModelToSample = _MasterModel
    
    
    l_SubsetModel = doCompareTwoModels(_MasterModel=_MasterModel, 
                                       _OtherModel=_OtherModel)
            




def doCompareTwoModels(_MasterModel, _OtherModel):
    
    l_DifferenceModel = st.ModelDifference()
    
    #Calculate diff between the axis from each model
    l_DifferenceModel.XAxisDifference = doCompareTwoAxis(_MasterAxis=_MasterModel.VibrationData.XAxis,
                                                         _OtherAxis=_OtherModel.VibrationData.XAxis)
    
    l_DifferenceModel.YAxisDifference = doCompareTwoAxis(_MasterAxis=_MasterModel.VibrationData.YAxis,
                                                         _OtherAxis=_OtherModel.VibrationData.YAxis)
    
    l_DifferenceModel.ZAxisDifference = doCompareTwoAxis(_MasterAxis=_MasterModel.VibrationData.ZAxis,
                                                         _OtherAxis=_OtherModel.VibrationData.ZAxis)
    
        
    return l_DifferenceModel
    
    
    
def doCompareTwoAxis(_MasterAxis, _OtherAxis):
    
    l_AxisDiff = st.AxisDifference()
    
    #Min diff
    l_AxisDiff.MinDiff = _MinDiff=f.getDifferenceBetweenValues(_Value1=_MasterAxis.Min, 
                                                                _Value2=_OtherAxis.Min)
    
    l_AxisDiff.MinDiff_prnt = _MinDiff_prnt=f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.Min,
                                                                                _Value2=_OtherAxis.Min)
    
    
    #Max diff
    l_AxisDiff.MaxDiff = MaxDiff=f.getDifferenceBetweenValues(_Value1=_MasterAxis.Max,
                                                                _Value2=_OtherAxis.Max)
    
    l_AxisDiff.MaxDiff_prnt = _MaxDiff_prnt=f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.Max,
                                                                                _Value2=_OtherAxis.Max)
    
    
    
    #Mean diff
    l_AxisDiff.MeanDiff = _MeanDiff=f.getDifferenceBetweenValues(_Value1=_MasterAxis.Mean,
                                                                    _Value2=_OtherAxis.Mean)
    
    l_AxisDiff.MeanDiff_prnt = _MeanDiff_prnt=f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.Mean,
                                                                                _Value2=_OtherAxis.Mean)
    
    
    #Std diff
    l_AxisDiff.StdDiff = _StdDiff=f.getDifferenceBetweenValues(_Value1=_MasterAxis.StandDev,
                                                                _Value2=_OtherAxis.StandDev)
    
    l_AxisDiff.StdDiff_prnt = _StdDiff_prnt=f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.StandDev,
                                                                                _Value2=_OtherAxis.StandDev)
    
    
    
    return l_AxisDiff
    
    





def doAddDataToVibrationAxis(_DataToAdd, _AxisName):
    
    l_NewAxis = st.VibrationAxis(_AxisName=_AxisName)
    
    l_NewAxis.RawData   = _DataToAdd
    
    #calculate max/min/etc for the new axis
    l_NewAxis.Max = f.doFindMaxInList(_Dataset=_DataToAdd)
    l_NewAxis.Min = f.doFindMinInList(_Dataset=_DataToAdd)
    
    l_NewAxis.Mean = f.doFindMeanInList(_Dataset=_DataToAdd)
    l_NewAxis.StandDev = f.doFindStandDevInList(_Dataset=_DataToAdd)
    
    
    return l_NewAxis
    


