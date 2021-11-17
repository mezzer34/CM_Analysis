from dataclasses import dataclass, field
from enum import Enum
from grpc.framework.common import style


@dataclass(order=True)
class VibrationAxis:
    AxisName: str

    RawData: list[float]

    Min: float
    Max: float
    Mean: float
    StandDev: float

    def __init__(self, _AxisName: str):
        self.AxisName = _AxisName
        self.RawData = []
        
        self.Min = 0
        self.Max = 0
        self.Mean = 0
        self.StandDev = 0

   

@dataclass(order=True)
class VibrationData:
    Time: list[float]
    XAxis: VibrationAxis
    YAxis: VibrationAxis
    ZAxis: VibrationAxis

    def __init__(self):
        self.Time = []
        self.XAxis = VibrationAxis(_AxisName="X")
        self.YAxis = VibrationAxis(_AxisName="Y")
        self.ZAxis = VibrationAxis(_AxisName="Z")

  


@dataclass(order=True)
class Model:
    Name: str
    OriginDate: str
    VibrationLog: VibrationData
    ModelLoaded: bool

    def __init__(self):
        self.Name = "NOT SET"
        self.OriginDate = "NOT_SET"
        self.VibrationLog = VibrationData()
        self.ModelLoaded = False

        



@dataclass(order=True)
class AxisDifference:
    MinDiff: float
    MaxDiff: float
    MeanDiff: float
    StandDevDiff: float

    MinDiff_prnt: float
    MaxDiff_prnt: float
    MeanDiff_prnt: float
    StandDevDiff_prnt: float
    
    RawDataDiff: list[float]
    RawDataDiff_prnt: list[float]

    def __init__(self):
        self.MinDiff = 0.0
        self.MaxDiff = 0.0
        self.MeanDiff = 0.0
        self.StandDevDiff = 0.0
        
        self.MinDiff_prnt = 0.0
        self.MaxDiff_prnt = 0.0
        self.MeanDiff_prnt = 0.0
        self.StandDevDiff_prnt = 0.0
        
        self.RawDataDiff = []
        self.RawDataDiff_prnt = []


@dataclass(order=True)
class ModelDifference:
    MasterName: str
    OtherName: str
    
    XAxis: AxisDifference
    YAxis: AxisDifference
    ZAxis: AxisDifference
    

    def __init__(self):
        self.MasterName = "NOT SET"
        self.OtherName = "NOT SET"
        
        self.XAxis = AxisDifference()
        self.YAxis = AxisDifference()
        self.ZAxis = AxisDifference()



@dataclass(order=True)
class ChartMetaData:
    ChartName: str
    
    YLims: list[float]
    
    YAxis_Label: str
    XAxis_Label: str
    
    LineLabels: list[str]
    
    Table: list[list[str]]
    
    
    def __init__(self):
        self.ChartName = "NOT SET"
        
        self.YLims = []
        
        self.YAxis_Label = "NOT SET"
        self.XAxis_Label = "NOT SET"
        
        self.LineLabels = []
        
        self.Table = []
    



@dataclass(order=True)
class FigureStruct:
    FigureName: str
    PageTitle: str
    
    Chart1_Meta: ChartMetaData
    Chart2_Meta: ChartMetaData
    
    Diff_Meta:   ChartMetaData
        
    ChartData: dict[str, list[float]]
    
    def __init__(self, _FigureName: str, _PageTitle: str):
        self.FigureName = "NOT SET"

        self.PageTitle = "NOT SET"

        self.Chart1_Meta = ChartMetaData()
        self.Chart2_Meta = ChartMetaData()
        
        self.Diff_Meta = ChartMetaData()
        
        self.ChartData = {} # dict[str, list[float]]





class PlotData(Enum):
    Master_Single_X = 1
    Master_Single_Y = 2
    Master_Single_Z = 3
    Master_All = 4
    
    MasterOther_Compare_X = 11
    MasterOther_Compare_Y = 12
    MasterOther_Compare_Z = 13
    MasterOther_Compare_All = 14
    
    MasterOther_Compare_X_WithDiff = 21
    MasterOther_Compare_Y_WithDiff = 22
    MasterOther_Compare_Z_WithDiff = 23
    MasterOther_Compare_All_WithDiff = 24
    
    

class ChartType(Enum):
    Lineplot = 1
    scatterplot = 2
    