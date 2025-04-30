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


def download_and_capture(youtube_id, source, start_seconds, quality):

    video_filename = f"{tmp_folder}/{youtube_id}_{start_seconds}_{quality}.webm"
    frame_id = f"ytid-{youtube_id}_sec-{start_seconds}"

    if (source == SourceOption.YT):
        download_youtube_video(youtube_id, start_seconds, video_filename, quality)
    else:
        return False
        
    output = tmp_folder + "/" + youtube_id

    # Create the folder if it doesn't exist
    os.makedirs(output, exist_ok=True)

    image_path = output + "/" + frame_id + ".jpeg"
        
    captured = save_image_from_video(video_filename, output_image=image_path)
    
    if captured:
        return Image.open(image_path)
    else:
        return False
                
