from enum import Enum

class QualityOption(str, Enum):
    '''
    Valid qualitys
    '''
    Q132 = "132"
    Q133 = "133"
    Q134 = "134"
    Q135 = "135"
    Q136 = "136"
    Q137 = "137"
    
class SourceOption(str, Enum):
    '''
    Valid video sources
    '''
    YT = "youtube"