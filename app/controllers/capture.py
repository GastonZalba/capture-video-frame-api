import os
import tempfile

import cv2
from PIL import Image

from .youtube import download_youtube_video
from ..enums import SourceOption

tmp_folder = f'{tempfile.gettempdir()}/ytdl'

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

    video_filename = f"{tmp_folder}/{youtube_id}_{start_seconds}_{resolution}.webm"
    frame_id = f"ytid-{youtube_id}_sec-{start_seconds}"
    
    output = tmp_folder + "/" + youtube_id

    image_path = output + "/" + frame_id + ".jpeg"

    # check if file is already downloaded
    if not os.path.isfile(image_path):

        if (source == SourceOption.YT):
            download_youtube_video(youtube_id, start_seconds, video_filename, resolution)
        else:
            return False

        # Create the folder if it doesn't exist
        os.makedirs(output, exist_ok=True)
            
        save_image_from_video(video_filename, output_image=image_path)
        
    return Image.open(image_path)
                
