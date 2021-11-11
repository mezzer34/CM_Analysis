from dataclasses import dataclass
from enum import Enum

@dataclass
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

   

@dataclass
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

  


@dataclass
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

        



@dataclass
class AxisDifference:
    MinDiff: float
    MaxDiff: float
    MeanDiff: float
    StandDevDiff: float

    MinDiff_prnt: float
    MaxDiff_prnt: float
    MeanDiff_prnt: float
    StandDevDiff_prnt: float

    def __init__(self):
        self.MinDiff = 0.0
        self.MaxDiff = 0.0
        self.MeanDiff = 0.0
        self.StandDevDiff = 0.0
        
        self.MinDiff_prnt = 0.0
        self.MaxDiff_prnt = 0.0
        self.MeanDiff_prnt = 0.0
        self.StandDevDiff_prnt = 0.0


@dataclass
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






class PlotData(Enum):
    Master_Single_X = 1
    Master_Single_Y = 2
    Master_Single_Z = 3
    Master_All = 4
    
    MasterOther_Compare_X = 11
    MasterOther_Compare_Y = 12
    MasterOther_Compare_Z = 13
    MasterOther_Compare_All = 14
    

class ChartType(Enum):
    Lineplot = 1
    Scatterplot = 2
    