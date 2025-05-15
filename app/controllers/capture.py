import os

import cv2
from PIL import Image

from .youtube import download_youtube_video
from ..enums import SourceOption
from ..params import TMP_FOLDER

def save_image_from_video(video_path, output_image):
    cap = cv2.VideoCapture(video_path)

    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    ret, frame = cap.read()
    captured = False
    
    if ret:
        cv2.imwrite(output_image, frame)
        captured = True
    else:
        captured = False        

    cap.release()
    
    return captured


def download_and_capture(youtube_id: str, source: SourceOption, start_seconds: float, resolution:str):

    video_filename = os.path.join(TMP_FOLDER, f"{youtube_id}_{start_seconds}_{resolution}.webm")
    frame_id = f"ytid-{youtube_id}_sec-{start_seconds}_{resolution}"
    
    output = os.path.join(TMP_FOLDER, youtube_id)
    
    os.makedirs(output, exist_ok=True)

    image_path = os.path.join(output, frame_id + ".jpeg")

    if (source == SourceOption.YT):
        download_youtube_video(youtube_id, start_seconds, video_filename, resolution)
    else:
        return False
        
    save_image_from_video(video_filename, output_image=image_path)
    
    # remove the webm temp file
    os.remove(video_filename)
    
    return Image.open(image_path)                
