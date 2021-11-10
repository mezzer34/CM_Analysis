from dataclasses import dataclass


@dataclass
class VibrationAxis:
    AxisName: str

    RawData: list[float()]

    Min: float
    Max: float
    Mean: float
    StandDev: float

    def __init__(self, _AxisName):
        self.AxisName = _AxisName
        self.RawData = []
        
        self.Min = 0
        self.Max = 0
        self.Mean = 0
        self.StandDev = 0

   

@dataclass
class VibrationData:
    Time: list[float()]
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
    VibrationData: VibrationData

    def __init__(self):
        self.Name = "Default"
        self.OriginDate = "NOT_SET"
        self.VibrationData = VibrationData()

        



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
    XAxis: AxisDifference
    YAxis: AxisDifference
    ZAxis: AxisDifference
    

    def __init__(self):
        self.XAxis = AxisDifference()
        self.YAxis = AxisDifference()
        self.ZAxis = AxisDifference()



