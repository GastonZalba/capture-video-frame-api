from enum import Enum
   
class SourceOption(str, Enum):
    '''
    Valid video sources
    '''
    YT = "youtube"
    
    
class VideoCodecOption(str, Enum):
    '''
    Valid video codec
    '''
    AVC1 = "avc1",
    VP09 = "vp09",
    VP9 = "vp9"
    