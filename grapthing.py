import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np
import pandas as pd
import seaborn as sns

import structs as st
import functions as f
import dataprocessing as processing


def doPlotModel(_MasterModel: st.Model, _OtherModel: st.Model, _ChartType: st.ChartType, _PlotData: st.PlotData):

    # Datasets have to be the same length!!
    # If the dataset is smaller than dont take a subset - just plot the whole thing
    # Use the same function to actually generate the list

    # NOTE - IF THE DATASET LENGTHS ARE DIFFERNET THEN THE OTHER MODEL WILL BE PLOTTED INCORRECTLY

    # USer selected subset size
    l_SubsetSize = 100

    # Check what subset size should be used
    if _MasterModel.VibrationLog.XAxis.RawData.__len__() < l_SubsetSize:
        l_SubsetSize = _MasterModel.VibrationLog.XAxis.RawData.__len__()

    # generate a index list to select from]
    l_IndexList = doGenerateIndexListToSelectFrom(_ListSize=len(_MasterModel.VibrationLog.XAxis.RawData),
                                                  _SubsetSize=l_SubsetSize)

    l_MasterList = doGenerateListOfDataFromModel(_Model=_MasterModel,
                                                 _IndexList=l_IndexList)
    l_OtherList = doGenerateListOfDataFromModel(_Model=_OtherModel,
                                                _IndexList=l_IndexList)

    l_TimeSubet = doGetSubsetOfList_float(_DataList=_MasterModel.VibrationLog.Time, 
                                          _IndexList=l_IndexList)

    l_DataDict = dict[str, list[float]]()
    l_MappingArray = list[list[str]]()

    l_DataDict["Time"] = l_TimeSubet

    # Check all lists to find the Y limits
    l_Master_YLim_Min = f.doFindMinInListOfLists(_ListOfDataset=l_MasterList)
    l_Master_YLim_Max = f.doFindMaxInListOfLists(_ListOfDataset=l_MasterList)

    l_Other_YLim_Min = f.doFindMinInListOfLists(_ListOfDataset=l_OtherList)
    l_Other_YLim_Max = f.doFindMaxInListOfLists(_ListOfDataset=l_OtherList)

    l_YLimits = [f.doFindMinInList([l_Master_YLim_Min, l_Other_YLim_Min]),
                 f.doFindMaxInList([l_Master_YLim_Max, l_Other_YLim_Max])]

    # add a % allowance to the top and bottom of the limits
    l_YLimits[0] = l_YLimits[0] - (l_YLimits[1] - l_YLimits[0]) * 0.1
    l_YLimits[1] = l_YLimits[1] + (l_YLimits[1] - l_YLimits[0]) * 0.1
    
    
    
    l_DifferenceData = processing.doCompareTwoModels(_MasterModel=_MasterModel,
                                                    _OtherModel= _OtherModel)
    
    
    l_DifferenceData.XAxis.RawDataDiff, l_DifferenceData.XAxis.RawDataDiff_prnt = processing.doFindDifferencesBetweenRawData(_MasterList=l_MasterList[0],
                                                                                                                             _OtherList=l_OtherList[0])

    l_DifferenceData.YAxis.RawDataDiff, l_DifferenceData.YAxis.RawDataDiff_prnt = processing.doFindDifferencesBetweenRawData(_MasterList=l_MasterList[1],
                                                                                                                             _OtherList=l_OtherList[1])
    
    l_DifferenceData.ZAxis.RawDataDiff, l_DifferenceData.ZAxis.RawDataDiff_prnt = processing.doFindDifferencesBetweenRawData(_MasterList=l_MasterList[2],
                                                                                                                             _OtherList=l_OtherList[2])
    
    
    
    # choose which type of chart to create
    if _PlotData == st.PlotData.Master_Single_X:

        l_MappingArray.append(["X Axis"])

        l_StringTitle = "v RMS X"
        l_DataDict[l_StringTitle] = l_MasterList[0]
        l_MappingArray.append(["Time", l_StringTitle])



    elif _PlotData == st.PlotData.Master_Single_Y:

        l_MappingArray.append(["Y Axis"])

        l_StringTitle = "v RMS Y"
        l_DataDict[l_StringTitle] = l_MasterList[1]
        l_MappingArray.append(["Time", l_StringTitle])



    elif _PlotData == st.PlotData.Master_Single_Z:

        l_MappingArray.append(["Z Axis"])

        l_StringTitle = "v RMS Z"
        l_DataDict[l_StringTitle] = l_MasterList[2]
        l_MappingArray.append(["Time", l_StringTitle])



    elif _PlotData == st.PlotData.Master_All:

        l_MappingArray.append(["All Master"])

        l_StringTitle = "v RMS X"
        l_DataDict[l_StringTitle] = l_MasterList[0]
        l_MappingArray.append(["Time", l_StringTitle])

        l_StringTitle = "v RMS Y"
        l_DataDict[l_StringTitle] = l_MasterList[1]
        l_MappingArray.append(["Time", l_StringTitle])

        l_StringTitle = "v RMS Z"
        l_DataDict[l_StringTitle] = l_MasterList[2]
        l_MappingArray.append(["Time", l_StringTitle])



    elif _PlotData == st.PlotData.MasterOther_Compare_X:

        l_MappingArray.append(["X Axis Comparison"])

        l_StringTitle = "v RMS A1 X"
        l_DataDict[l_StringTitle] = l_MasterList[0]
        l_MappingArray.append(["Time", l_StringTitle])

        l_StringTitle = "v RMS A2 X"
        l_DataDict[l_StringTitle] = l_OtherList[0]
        l_MappingArray.append(["Time", l_StringTitle])



    elif _PlotData == st.PlotData.MasterOther_Compare_Y:

        l_MappingArray.append(["Y Axis Comparison"])

        l_StringTitle = "v RMS A1 Y"
        l_DataDict[l_StringTitle] = l_MasterList[1]
        l_MappingArray.append(["Time", l_StringTitle])

        l_StringTitle = "v RMS A2 Y"
        l_DataDict[l_StringTitle] = l_OtherList[1]
        l_MappingArray.append(["Time", l_StringTitle])



    elif _PlotData == st.PlotData.MasterOther_Compare_Z:

        l_MappingArray.append(["Z Axis Comparison"])

        l_StringTitle = "v RMS A1 Z"
        l_DataDict[l_StringTitle] = l_MasterList[2]
        l_MappingArray.append(["Time", l_StringTitle])

        l_StringTitle = "v RMS A2 Z"
        l_DataDict[l_StringTitle] = l_OtherList[2]
        l_MappingArray.append(["Time", l_StringTitle])



    elif _PlotData == st.PlotData.MasterOther_Compare_All:

        l_MappingArray.append(["All Master Comparison"])

        l_MappingArray.append([_MasterModel.Name])

        l_StringTitle = "v RMS A1 X"
        l_DataDict[l_StringTitle] = l_MasterList[0]
        l_MappingArray[1].extend(["Time", l_StringTitle])

        l_StringTitle = "v RMS A1 Y"
        l_DataDict[l_StringTitle] = l_MasterList[1]
        l_MappingArray[1].extend([l_StringTitle])

        l_StringTitle = "v RMS A1 Z"
        l_DataDict[l_StringTitle] = l_MasterList[2]
        l_MappingArray[1].extend([l_StringTitle])

        l_MappingArray.append([_OtherModel.Name])

        l_StringTitle = "v RMS A2 Y"
        l_DataDict[l_StringTitle] = l_OtherList[1]
        l_MappingArray[2].extend([l_StringTitle])

        l_StringTitle = "v RMS A2 X"
        l_DataDict[l_StringTitle] = l_OtherList[0]
        l_MappingArray[2].extend(["Time", l_StringTitle])

        l_StringTitle = "v RMS A2 Z"
        l_DataDict[l_StringTitle] = l_OtherList[2]
        l_MappingArray[2].extend([l_StringTitle])



    elif _PlotData == st.PlotData.MasterOther_Compare_All_WithDiff:

        l_MappingArray.append(["All Master Comparison"])

        l_MappingArray.append([_MasterModel.Name])
        
        
        l_ListForTable = list[list[list[str]]]()
        
        
       
        l_ListForTable.append(doGenerateListForTable_Model(_Model = _MasterModel))
        l_ListForTable.append(doGenerateListForTable_Model(_Model = _OtherModel))
        
        l_ListForTable.append(doGenerateListForTable_Diff(_Diff = l_DifferenceData))
        
        
                
        l_StringTitle = "v RMS A1 X"
        l_DataDict[l_StringTitle] = l_MasterList[0]
        l_MappingArray[1].extend(["Time", l_StringTitle])

        l_StringTitle = "v RMS A1 Y"
        l_DataDict[l_StringTitle] = l_MasterList[1]
        l_MappingArray[1].extend([l_StringTitle])

        l_StringTitle = "v RMS A1 Z"
        l_DataDict[l_StringTitle] = l_MasterList[2]
        l_MappingArray[1].extend([l_StringTitle])

        l_MappingArray.append([_OtherModel.Name])

        l_StringTitle = "v RMS A2 X"
        l_DataDict[l_StringTitle] = l_OtherList[0]
        l_MappingArray[2].extend(["Time", l_StringTitle])

        l_StringTitle = "v RMS A2 Y"
        l_DataDict[l_StringTitle] = l_OtherList[1]
        l_MappingArray[2].extend([l_StringTitle])

        l_StringTitle = "v RMS A2 Z"
        l_DataDict[l_StringTitle] = l_OtherList[2]
        l_MappingArray[2].extend([l_StringTitle])

        l_MappingArray.append(["Differential Examination"])

        l_StringTitle = "v RMS X - Diff"
        l_DataDict[l_StringTitle] = l_DifferenceData.XAxis.RawDataDiff
        l_MappingArray[3].extend(["Time", l_StringTitle])

        l_StringTitle = "v RMS Y - Diff"
        l_DataDict[l_StringTitle] = l_DifferenceData.YAxis.RawDataDiff
        l_MappingArray[3].extend([l_StringTitle])

        l_StringTitle = "v RMS Z - Diff"
        l_DataDict[l_StringTitle] = l_DifferenceData.ZAxis.RawDataDiff
        l_MappingArray[3].extend([l_StringTitle])



    else:
        print("Error - Plot Data Type not recognised")

    # generate a dataframe from the dictionary
    l_Dataframe = pd.DataFrame(l_DataDict)
    
    

    # plot the dataframe
    if _ChartType == st.ChartType.Lineplot:
        doLineplot_OfDataframe(_Dataframe=l_Dataframe,
                               _MappingArray=l_MappingArray,
                               _YLim=l_YLimits,
                               _ListForTable=l_ListForTable)
        
        

    elif _ChartType == st.ChartType.scatterplot:
        doScatterplot_OfDataFrame(_Dataframe=l_Dataframe,
                                  _MappingArray=l_MappingArray)
        
    
    # generate a list to use for legend
    l_LegendList = list[str]()
    for i in range(2, len(l_MappingArray[1])):
        l_LegendList.append(l_MappingArray[1][i])

    plt.legend(loc="upper right",
               labels=l_LegendList)
    
    


def doGenerateIndexListToSelectFrom(_ListSize: int, _SubsetSize: int):
    # create a list of data from each model
    l_IndexList = list[int]()

    # calculate the step size
    l_Step = int(np.floor(_ListSize / _SubsetSize))

    # step cannot be less than 1
    if l_Step < 1:
        l_Step = 1

    # generate the list
    for l_Index in range(0, _ListSize, l_Step):
        l_IndexList.append(l_Index)

    return l_IndexList


def doGetSubsetOfList_float(_DataList: list[float], _IndexList: list[int]):
    l_SubsetOfList = list[float]()
    l_Index = int()

    for l_Index in _IndexList:
        # check if the index is out of range
        if l_Index > len(_DataList) - 1:
            l_SubsetOfList.append(0)
        else:
            l_SubsetOfList.append(_DataList[l_Index])

    return l_SubsetOfList


def doGetSubsetOfList_int(_DataList: list[int], _IndexList: list[int]):
    l_SubsetOfList = list[int]()
    l_Index = int()

    for l_Index in _IndexList:
        l_SubsetOfList.append(_DataList[l_Index])

    return l_SubsetOfList


def doGenerateListOfDataFromModel(_Model: st.Model, _IndexList: list[int]):
    # create a list of data from each model
    l_ModelDataList = list[list[float]]()
    l_ModelDataList.append(doGetSubsetOfList_float(_DataList=_Model.VibrationLog.XAxis.RawData,
                                                   _IndexList=_IndexList))

    l_ModelDataList.append(doGetSubsetOfList_float(_DataList=_Model.VibrationLog.YAxis.RawData,
                                                   _IndexList=_IndexList))

    l_ModelDataList.append(doGetSubsetOfList_float(_DataList=_Model.VibrationLog.ZAxis.RawData,
                                                   _IndexList=_IndexList))

    return l_ModelDataList


def doPrintMappingArray(_MappingArray: list[list[str]]):

    for i in range(0, len(_MappingArray)):
        print(" | " + str(i) + ": " + str(_MappingArray[i]))

        for x in range(0, len(_MappingArray[i])):
            print(" | -- " + str(x) + ": " + str(_MappingArray[i][x]))


def doGetYLimits(_DataList: list[float]):
    l_YLimits = list[float]()
    l_YLimits.append(min(_DataList))
    l_YLimits.append(max(_DataList))

    return l_YLimits


def doExtendList(_Value: float, _FinalSize: int):
    l_ExtendedList = list[float]()

    for i in range(0, _FinalSize):
        l_ExtendedList.append(_Value)

    return l_ExtendedList


def doGenerateListForTable_Model(_Model: st.Model):
     #Generate a list of all required information
    l_ListLine = list[str]()
    l_IndividualTable = list[list[str]]()
    
    l_ListLine = ["Max",
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.XAxis.Max, 2,3), 
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.YAxis.Max, 2,3), 
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.ZAxis.Max, 2,3)]
    l_IndividualTable.append(l_ListLine)
    
    l_ListLine = ["Min",
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.XAxis.Min, 2,3), 
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.YAxis.Min, 2,3), 
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.ZAxis.Min, 2,3)]
    l_IndividualTable.append(l_ListLine)
    
    l_ListLine = ["Mean",
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.XAxis.Mean, 2,3),
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.YAxis.Mean, 2,3),
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.ZAxis.Mean, 2,3)]
    l_IndividualTable.append(l_ListLine)
    
    l_ListLine = ["Std",
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.XAxis.StandDev, 2,3),
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.YAxis.StandDev, 2,3),
                  f.doGetNumberOfFixedLength(_Model.VibrationLog.ZAxis.StandDev, 2,3)]
    l_IndividualTable.append(l_ListLine)
                  
            
    return l_IndividualTable




def doGenerateListForTable_Diff(_Diff: st.ModelDifference):
     #Generate a list of all required information
    l_ListLine = list[str]()
    l_IndividualTable = list[list[str]]()
    
    
    l_ListLine = ["Max",
                    f.doGetNumberOfFixedLength(_Diff.XAxis.MaxDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.XAxis.MaxDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.YAxis.MaxDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.YAxis.MaxDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.ZAxis.MaxDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.ZAxis.MaxDiff_prnt, 2, 3) + "%)"]
    l_IndividualTable.append(l_ListLine)
            
     
     
    l_ListLine = ["Min",
                    f.doGetNumberOfFixedLength(_Diff.XAxis.MinDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.XAxis.MinDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.YAxis.MinDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.YAxis.MinDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.ZAxis.MinDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.ZAxis.MinDiff_prnt, 2, 3) + "%)"]
    l_IndividualTable.append(l_ListLine)
    
               
     
    l_ListLine = ["Mean",
                    f.doGetNumberOfFixedLength(_Diff.XAxis.MeanDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.XAxis.MeanDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.YAxis.MeanDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.YAxis.MeanDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.ZAxis.MeanDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.ZAxis.MeanDiff_prnt, 2, 3) + "%)"]
    l_IndividualTable.append(l_ListLine)
    
               
     
    l_ListLine = ["Std",
                    f.doGetNumberOfFixedLength(_Diff.XAxis.StandDevDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.XAxis.StandDevDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.YAxis.StandDevDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.YAxis.StandDevDiff_prnt, 2, 3) + "%)",
                    f.doGetNumberOfFixedLength(_Diff.ZAxis.StandDevDiff, 2,3) + "("+ f.doGetNumberOfFixedLength(_Diff.ZAxis.StandDevDiff_prnt, 2, 3) + "%)"]
    l_IndividualTable.append(l_ListLine)
    
    
    return l_IndividualTable




def doLineplot_OfDataframe(_Dataframe: pd.DataFrame, _MappingArray: list[list[str]], _YLim: list[float], _ListForTable: list[list[list[str]]]):

    # Plot a chart for each top level dimension of the mapping list
    fig, axes = plt.subplots(nrows=2, ncols=len(_MappingArray) - 1, figsize=(18, 9))
    
    fig.suptitle(_MappingArray[0][0])

    doPrintMappingArray(_MappingArray=_MappingArray)

    print(_Dataframe)

    # set the title of each chart, and plot the data
    for i in range(0, len(_MappingArray) - 1):
        axes[0, i].set_title(_MappingArray[i + 1][0])

        axes[0, i].set(ylim=(_YLim[0], _YLim[1]))
        
        axes[1, i].axis("off")
        
        if i < len(_MappingArray) - 1:
            
            axes[1, i].axis("tight")
            axes[1, i].axis("off")
            
            
            axes[1, i].table(cellText=_ListForTable[i], 
                             cellLoc = "center",
                             loc="best",
                             colLabels = ["-", "X", "Y", "Z"])
                             
             
        


        for n in range(2, len(_MappingArray[i + 1])):
            sns.lineplot(ax=axes[0, i], x="Time", y=_MappingArray[i + 1][n], data=_Dataframe)
            
    
    
    
    
    

def doScatterplot_OfDataFrame(_Dataframe: pd.DataFrame, _MappingArray: list[list[str]]):

    # Plot a chart for each top level dimension of the mapping list
    fig, axes = plt.subplots(nrows=1, ncols=len(_MappingArray) - 1)

    fig.suptitle(_MappingArray[0][0])

    # set the title of each chart, and plot the data
    for i in range(0, len(_MappingArray) - 1):
        axes[i].set_title(_MappingArray[i + 1][0])

        for n in range(2, len(_MappingArray[i])):
            sns.scatterplot(ax=axes[i], x="Time",
                            y=_MappingArray[i + 1][n], data=_Dataframe)


