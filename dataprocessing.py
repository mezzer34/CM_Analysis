import functions as f
import structs as st

import file_func as file_func



def doLoadFromCSVAndConvertToModel(_DirectoryPath: str,_MaxNumberOfFilesToSelect: int):
    l_UserFileNameSelection = list[str]()
    l_UserFileNameSelection = file_func.doGetFileNameSelectionFromUser(_MaxNumberOfFilesToSelect=_MaxNumberOfFilesToSelect, 
                                                                       _DirectoryPath=_DirectoryPath)


    #Get useable data from file name
    l_LoadedVibrationDataList = list[st.VibrationData]()
    l_LoadedVibrationDataList = doLoadCSVAndStoreAsVibrationDataStruct(_UserFileNameSelection=l_UserFileNameSelection)
    
    
    #Convert list of vibration data to models
    l_NewModelsList = list[st.Model]()
    l_Data = st.Model()
    for l_Data in l_LoadedVibrationDataList:
        l_NewModelsList.append(doGenerateModelFromDataset(l_Data, "TestModel"))


    return l_NewModelsList



def doLoadCSVAndStoreAsVibrationDataStruct(_UserFileNameSelection: list[str]):
    l_VibrationLogList = list[st.VibrationData]()
    for l_FileName in _UserFileNameSelection:        
        l_VibrationLogList.append(doLoadFileAndConvertToVibrationDataStruct(_FileToLoad=l_FileName))
        
    
    return l_VibrationLogList
    

    
    
def doLoadFileAndConvertToVibrationDataStruct(_FileToLoad: str):

    # open files from user selection and load data
    l_LoadedLines = file_func.doLoadDataFromSelectedFile(_FileToLoad=_FileToLoad)
    
    l_LoadedLines = f.doTrimLines(lines=l_LoadedLines, 
                                    front_trim=3, 
                                    back_trim=0)
    
    l_Time = list[float]()
    l_X = list[float]()
    l_Y = list[float]()
    l_Z = list[float]()

    l_Time, l_X, l_Y, l_Z = doGenerateRawVibrationDataLists(_LoadedLines=l_LoadedLines)

 
    
    #add the data to a vibration data object
    l_VibrationLog = st.VibrationData()
    
    l_VibrationLog.Time =l_Time
    
    l_VibrationLog.XAxis = doAddDataToVibrationAxis(_DataToAdd=l_X, _AxisName="X")
    l_VibrationLog.YAxis = doAddDataToVibrationAxis(_DataToAdd=l_Y, _AxisName="Y")
    l_VibrationLog.ZAxis = doAddDataToVibrationAxis(_DataToAdd=l_Z, _AxisName="Z")
       
    
    return l_VibrationLog





def doGenerateRawVibrationDataLists(_LoadedLines: list[str]):
   
    Time = list[float]()
    X = list[float]()
    Y = list[float]()
    Z = list[float]()

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




def doGenerateModelFromDataset(_VibrationData: st.VibrationData, _ModelName: str):
    
    l_NewModel = st.Model()
    
    l_NewModel.Name = _ModelName
    
    
    #set origin date to now
    l_NewModel.OriginDate = f.getCurrentSystemDateTime()
    
    
    l_NewModel.VibrationLog = _VibrationData
    
    l_NewModel.ModelLoaded = True    
       
      
    return l_NewModel




    
def doCreateComparrisonBetweenTwoModels(_MasterModel: st.Model, _OtherModel: st.Model):
    #get the data from the model 
        
    l_ComparrisonModel = doCompareTwoModels(_MasterModel=_MasterModel, 
                                       _OtherModel=_OtherModel)
            

    return l_ComparrisonModel



def doCompareTwoModels(_MasterModel: st.Model, _OtherModel: st.Model):
    
    l_DifferenceModel = st.ModelDifference()
    
    
    _MasterModel.VibrationLog.XAxis
    
    #Calculate diff between the axis from each model
    l_DifferenceModel.XAxis = doCompareTwoAxis(_MasterAxis=_MasterModel.VibrationLog.XAxis,
                                                _OtherAxis=_OtherModel.VibrationLog.XAxis)
    
    l_DifferenceModel.YAxis = doCompareTwoAxis(_MasterAxis=_MasterModel.VibrationLog.YAxis,
                                                _OtherAxis=_OtherModel.VibrationLog.YAxis)
    
    l_DifferenceModel.ZAxis = doCompareTwoAxis(_MasterAxis=_MasterModel.VibrationLog.ZAxis,
                                                _OtherAxis=_OtherModel.VibrationLog.ZAxis)
    
        
    return l_DifferenceModel
    
    
    
def doCompareTwoAxis(_MasterAxis: st.VibrationAxis, _OtherAxis: st.VibrationAxis):
    
    l_AxisDiff = st.AxisDifference()
    
    #Min diff
    l_AxisDiff.MinDiff = f.getDifferenceBetweenValues(_Value1=_MasterAxis.Min, 
                                                    _Value2=_OtherAxis.Min)
    
    l_AxisDiff.MinDiff_prnt = f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.Min,
                                                                _Value2=_OtherAxis.Min)
    
    
    #Max diff
    l_AxisDiff.MaxDiff = f.getDifferenceBetweenValues(_Value1=_MasterAxis.Max,
                                                                _Value2=_OtherAxis.Max)
    
    l_AxisDiff.MaxDiff_prnt = f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.Max,
                                                                _Value2=_OtherAxis.Max)
    
    
    
    #Mean diff
    l_AxisDiff.MeanDiff = f.getDifferenceBetweenValues(_Value1=_MasterAxis.Mean,
                                                                    _Value2=_OtherAxis.Mean)
    
    l_AxisDiff.MeanDiff_prnt = f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.Mean,
                                                                _Value2=_OtherAxis.Mean)
    
    
    #Std diff
    l_AxisDiff.StandDevDiff = f.getDifferenceBetweenValues(_Value1=_MasterAxis.StandDev,
                                                            _Value2=_OtherAxis.StandDev)
    
    l_AxisDiff.StandDevDiff_prnt = f.getPrcntDifferenceBetweenValues(_Value1=_MasterAxis.StandDev,
                                                                    _Value2=_OtherAxis.StandDev)
    
    
    
    return l_AxisDiff
    
    





def doAddDataToVibrationAxis(_DataToAdd: list[float], _AxisName: str):
    
    l_NewAxis = st.VibrationAxis(_AxisName=_AxisName)
    
    l_NewAxis.RawData   = _DataToAdd
    
    #calculate max/min/etc for the new axis
    l_NewAxis.Max = f.doFindMaxInList(_Dataset=_DataToAdd)
    l_NewAxis.Min = f.doFindMinInList(_Dataset=_DataToAdd)
    
    l_NewAxis.Mean = f.doFindMeanInList(_Dataset=_DataToAdd)
    l_NewAxis.StandDev = f.doFindStandDevInList(_Dataset=_DataToAdd)
    
    
    return l_NewAxis
    


