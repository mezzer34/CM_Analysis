import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np
import pandas as pd
import seaborn as sns


import typing

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

    
    
    l_FigureStructure = st.FigureStruct(_FigureName = "-", 
                                        _PageTitle = "-")
    
    
    l_FigureStructure.ChartData["Time (s)"] = doGetSubsetOfList_float(_DataList=_MasterModel.VibrationLog.Time, 
                                                                        _IndexList=l_IndexList)
    
    

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
    
    
    l_FigureStructure.Chart1_Meta.YLims = l_YLimits
    l_FigureStructure.Chart2_Meta.YLims = l_YLimits
    l_FigureStructure.Diff_Meta.YLims = l_YLimits
    
    
    l_DifferenceData = processing.doCompareTwoModels(_MasterModel=_MasterModel,
                                                    _OtherModel= _OtherModel)
    
    
    l_DifferenceData.XAxis.RawDataDiff, l_DifferenceData.XAxis.RawDataDiff_prnt = processing.doFindDifferencesBetweenRawData(_MasterList=l_MasterList[0],
                                                                                                                             _OtherList=l_OtherList[0])

    l_DifferenceData.YAxis.RawDataDiff, l_DifferenceData.YAxis.RawDataDiff_prnt = processing.doFindDifferencesBetweenRawData(_MasterList=l_MasterList[1],
                                                                                                                             _OtherList=l_OtherList[1])
    
    l_DifferenceData.ZAxis.RawDataDiff, l_DifferenceData.ZAxis.RawDataDiff_prnt = processing.doFindDifferencesBetweenRawData(_MasterList=l_MasterList[2],
                                                                                                                             _OtherList=l_OtherList[2])
    
    l_List = list[list[str]]()
    
    # choose which type of chart to create
    if _PlotData == st.PlotData.Master_Single_X:
        l_FigureStructure.FigureName = _MasterModel.Name + " - X Axis"
        l_FigureStructure.PageTitle = _MasterModel.Name + " - X Axis"
                
        l_List = [["Vel RMS X"]]
        
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]        
        l_FigureStructure.ChartData[l_List[0][0]] = l_MasterList[0]

    elif _PlotData == st.PlotData.Master_Single_Y:
        l_FigureStructure.FigureName = _MasterModel.Name + " - Y Axis"
        l_FigureStructure.PageTitle = _MasterModel.Name + " - Y Axis"
                
        l_List = [["Vel RMS Y"]]
        
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]        
        l_FigureStructure.ChartData[l_List[0][0]] = l_MasterList[1]

    elif _PlotData == st.PlotData.Master_Single_Z:
        l_FigureStructure.FigureName = _MasterModel.Name + " - Z Axis"
        l_FigureStructure.PageTitle = _MasterModel.Name + " - Z Axis"
        
        l_List = [["Vel RMS Z"]]        
        
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]        
        l_FigureStructure.ChartData[l_List[0][0]] = l_MasterList[2]

    elif _PlotData == st.PlotData.Master_All:
        l_FigureStructure.FigureName = _MasterModel.Name
        l_FigureStructure.PageTitle = _MasterModel.Name
        
        l_List = [["Vel RMS X", "Vel RMS Y", "Vel RMS Z"]]     
        
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
              
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]    
        l_FigureStructure.ChartData[l_List[0][0]] = l_MasterList[0]
      
        l_FigureStructure.ChartData[l_List[0][1]] = l_MasterList[1]
   
        l_FigureStructure.ChartData[l_List[0][2]] = l_MasterList[2]
    


    elif _PlotData == st.PlotData.MasterOther_Compare_X:
        l_FigureStructure.FigureName = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name + " - X Axis"
        l_FigureStructure.PageTitle = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name + " - X Axis"
        
        l_List = [["Vel RMS A1 X"], ["Vel RMS A2 X"]]        
        
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]       
        l_FigureStructure.ChartData[l_List[0][0]] = l_MasterList[0]
        
        
        l_FigureStructure.Chart2_Meta.ChartName = _OtherModel.Name
        
        l_FigureStructure.Chart2_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart2_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart2_Meta.LineLabels = l_List[1]       
        l_FigureStructure.ChartData[l_List[1][0]] = l_OtherList[0]
        


    elif _PlotData == st.PlotData.MasterOther_Compare_Y:
        l_FigureStructure.FigureName = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name + " - Y Axis"
        l_FigureStructure.PageTitle = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name + " - Y Axis"
                
        l_List = [["Vel RMS A1 Y"], ["Vel RMS A2 Y"]]        
        
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
               
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]       
        l_FigureStructure.ChartData[l_List[0][1]] = l_MasterList[1]
        
        
        l_FigureStructure.Chart2_Meta.ChartName = _OtherModel.Name
        
        l_FigureStructure.Chart2_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart2_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart2_Meta.LineLabels = l_List[1]       
        l_FigureStructure.ChartData[l_List[1][1]] = l_OtherList[1]
        


    elif _PlotData == st.PlotData.MasterOther_Compare_Z:
        l_FigureStructure.FigureName = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name + " - Z Axis"
        l_FigureStructure.PageTitle = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name + " - Z Axis"
                
        l_List = [["Vel RMS A1 Z"], ["Vel RMS A2 Z"]]           
        
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
            
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]       
        l_FigureStructure.ChartData[l_List[0][2]] = l_MasterList[2]
        
        
        l_FigureStructure.Chart2_Meta.ChartName = _OtherModel.Name
        
        l_FigureStructure.Chart2_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart2_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart2_Meta.LineLabels = l_List[1]       
        l_FigureStructure.ChartData[l_List[1][2]] = l_OtherList[2]



    elif _PlotData == st.PlotData.MasterOther_Compare_All:
        l_FigureStructure.FigureName = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name
        l_FigureStructure.PageTitle = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name
        
        
        l_List = [["Vel RMS A1 X", "Vel RMS A1 Y", "Vel RMS A1 Z"], 
                  ["Vel RMS A2 X", "Vel RMS A2 Y", "Vel RMS A2 Z"]]
                                     
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]    
        l_FigureStructure.ChartData[l_List[0][0]] = l_MasterList[0]
      
        l_FigureStructure.ChartData[l_List[0][1]] = l_MasterList[1]
   
        l_FigureStructure.ChartData[l_List[0][2]] = l_MasterList[2]
        
        
        l_FigureStructure.Chart2_Meta.ChartName = _OtherModel.Name    
        
        l_FigureStructure.Chart2_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart2_Meta.YAxis_Label = "VIbration Vel (mm/s)"

        l_FigureStructure.Chart2_Meta.LineLabels = l_List[1]    
        l_FigureStructure.ChartData[l_List[1][0]] = l_OtherList[0]
      
        l_FigureStructure.ChartData[l_List[1][1]] = l_OtherList[1]
   
        l_FigureStructure.ChartData[l_List[1][2]] = l_OtherList[2]
        
        
        

    elif _PlotData == st.PlotData.MasterOther_Compare_All_WithDiff:
        l_FigureStructure.FigureName = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name
        l_FigureStructure.PageTitle = "Axis Comparison - " + _MasterModel.Name + " & " + _OtherModel.Name
        
        
        
        l_List = [["Vel RMS A1 X", "Vel RMS A1 Y", "Vel RMS A1 Z"], 
                  ["Vel RMS A2 X", "Vel RMS A2 Y", "Vel RMS A2 Z"],
                  ["Vel RMS X - Diff", "Vel RMS Y - Diff", "Vel RMS Z - Diff"]]
               
        
        l_FigureStructure.Chart1_Meta.ChartName = _MasterModel.Name
        
        l_FigureStructure.Chart1_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart1_Meta.YAxis_Label = "VIbration Vel (mm/s)"
                           
        l_FigureStructure.Chart1_Meta.LineLabels = l_List[0]    
        l_FigureStructure.ChartData[l_List[0][0]] = l_MasterList[0]
      
        l_FigureStructure.ChartData[l_List[0][1]] = l_MasterList[1]
   
        l_FigureStructure.ChartData[l_List[0][2]] = l_MasterList[2]

        l_FigureStructure.Chart1_Meta.Table = doGenerateListForTable_Model(_Model = _MasterModel)
        
        
        l_FigureStructure.Chart2_Meta.ChartName = _OtherModel.Name   
        
        l_FigureStructure.Chart2_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Chart2_Meta.YAxis_Label = "VIbration Vel (mm/s)" 
        
        l_FigureStructure.Chart2_Meta.LineLabels = l_List[1]    
        l_FigureStructure.ChartData[l_List[1][0]] = l_OtherList[0]
      
        l_FigureStructure.ChartData[l_List[1][1]] = l_OtherList[1]
   
        l_FigureStructure.ChartData[l_List[1][2]] = l_OtherList[2]

        l_FigureStructure.Chart2_Meta.Table = doGenerateListForTable_Model(_Model = _OtherModel)
        
        
        
        l_FigureStructure.Diff_Meta.ChartName = "Abs Difference"  
        
        l_FigureStructure.Diff_Meta.XAxis_Label = "Time (s)"
        l_FigureStructure.Diff_Meta.YAxis_Label = "VIbration Vel (mm/s)"
        
        l_FigureStructure.Diff_Meta.LineLabels = l_List[2]    
        l_FigureStructure.ChartData[l_List[2][0]] = l_DifferenceData.XAxis.RawDataDiff
      
        l_FigureStructure.ChartData[l_List[2][1]] = l_DifferenceData.YAxis.RawDataDiff
   
        l_FigureStructure.ChartData[l_List[2][2]] = l_DifferenceData.ZAxis.RawDataDiff

        l_FigureStructure.Diff_Meta.Table = doGenerateListForTable_Diff(_Diff = l_DifferenceData)
        
        
    else:
        print("Error - Plot Data Type not recognised")



    # plot the dataframe
    if _ChartType == st.ChartType.Lineplot:
        doLineplot_OfDataframe(_FigureStrucutre = l_FigureStructure)
        
        
    
    """ # generate a list to use for legend
    l_LegendList = list[str]()
    for i in range(2, len(l_MappingArray[1])):
        l_LegendList.append(l_MappingArray[1][i])


    plt.legend(loc="upper right",
               labels=l_LegendList)
     """
    


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


def doPrintFigureStruct(_FigureStruct: st.FigureStruct):
    doPrintChartMetaData(_ChartStruct = _FigureStruct.Chart1_Meta)
    doPrintChartMetaData(_ChartStruct = _FigureStruct.Chart2_Meta)
    doPrintChartMetaData(_ChartStruct = _FigureStruct.Diff_Meta)

    #print data dict
    
    return


def doPrintChartMetaData(_ChartStruct: st.ChartMetaData):
    #Print meta data
    print("Chart Name: " + _ChartStruct.ChartName)
    
    print(" |       Y-Limits" + str(_ChartStruct.YLims))
    
    print(" |       X-Axis Label: " + _ChartStruct.YAxis_Label)
    print(" |       Y-Axis Label: " + _ChartStruct.XAxis_Label)
    
    print(" |       Line Labels: " + str(_ChartStruct.LineLabels))
    
    print(" |       Table: " + str(_ChartStruct.Table))
        
    return





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
    
    
    
def doGenerateChartInfoAsList(_Title: str, _YAxis_Label: str, _Model: st.Model, _LineTitles: list[str]):
    l_ChartInfoList = list[list[list[str]]]()
    
    l_ChartInfoList.append([[_Title]])
    
    l_ChartInfoList.append([[ _YAxis_Label ]])
    l_ChartInfoList.append([_LineTitles])
    
    l_ChartInfoList.append(doGenerateListForTable_Model(_Model = _Model))
        

    return l_ChartInfoList

    
    
def doGenerateChartDiffInfoAsList(_Title: str, _YAxis_Label: str, _ModelDiff: st.ModelDifference, _LineTitles: list[str]):
    l_ChartInfoList = list[list[list[str]]]()
    
    l_ChartInfoList.append([[_Title]])
    
    l_ChartInfoList.append([[ _YAxis_Label ]])
    l_ChartInfoList.append([_LineTitles])
    
    l_ChartInfoList.append(doGenerateListForTable_Diff(_Diff = _ModelDiff))
        

    return l_ChartInfoList





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




def doLineplot_OfDataframe(_FigureStrucutre: st.FigureStruct):
    
    #Check how many charts should be plotted
    l_NumberOfCharts = 1
    if _FigureStrucutre.Chart2_Meta.ChartName != "":
        l_NumberOfCharts = 2
        
    if _FigureStrucutre.Diff_Meta.ChartName != "":
        l_NumberOfCharts = l_NumberOfCharts + 1
    
    
    #Generate a dataframe 
    l_Dataframe = pd.DataFrame(_FigureStrucutre.ChartData)
    
    
    doPrintFigureStruct(_FigureStruct = _FigureStrucutre)
    
    print(l_Dataframe)
    
    # Plot a chart for each top level dimension of the mapping list
    fig, axes = plt.subplots(nrows=2, ncols=l_NumberOfCharts, figsize=(18, 9))
    
    fig.suptitle(_FigureStrucutre.PageTitle, fontsize=16)
    
    l_ChartMetaData = st.ChartMetaData()
    for i in range(0, l_NumberOfCharts):
        #get the chart to plot
        if i == 0:
            l_ChartMetaData = _FigureStrucutre.Chart1_Meta
            
        elif i == 1:
            l_ChartMetaData = _FigureStrucutre.Chart2_Meta
            
        elif i == 2:
            l_ChartMetaData = _FigureStrucutre.Diff_Meta
            
            
        axes[0, i].set_title(l_ChartMetaData.ChartName)

        axes[0, i].set(ylim=l_ChartMetaData.YLims)
        
        axes[0, i].set(xlabel=l_ChartMetaData.XAxis_Label)
        axes[0, i].set(ylabel=l_ChartMetaData.YAxis_Label)
        
        
        axes[1, i].axis("off")
        
        
        axes[1, i].axis("tight")
        axes[1, i].axis("off")
        
        
        axes[1, i].table(cellText=l_ChartMetaData.Table,
                        cellLoc = "center",
                        loc="best",
                        colLabels = ["-", "X", "Y", "Z"])
                        
        
        


        for n in range(0, len(l_ChartMetaData.LineLabels)):
            sns.lineplot(ax=axes[0, i], x = "Time (s)", y = l_ChartMetaData.LineLabels[n], data=l_Dataframe)
            
    
        
    
