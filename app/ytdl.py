import os
import tempfile
from PIL import Image

import yt_dlp
from yt_dlp.utils import download_range_func

from .capture import capture_frame
from .enums import SourceOption

tmp_folder = f'{tempfile.gettempdir()}/ytdl'

def download_youtube_video(youtube_id, start_seconds, video_filename, quality):
    ydl_opts = {
        "verbose": False,
        "format": quality,
        "outtmpl": video_filename,
        "download_ranges": download_range_func(None, [(start_seconds, start_seconds + 0.1)]),
        "force_keyframes_at_cuts": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://www.youtube.com/watch?v=" + youtube_id])

def download_and_capture(youtube_id, source, start_seconds, quality):

    video_filename = f"tmp/{youtube_id}_{start_seconds}_{quality}.webm"
    frame_id = f"ytid-{youtube_id}_sec-{start_seconds}"

    if (source == SourceOption.YT):
        download_youtube_video(youtube_id, start_seconds, video_filename, quality)
    else:
        return False
        
    output = tmp_folder + "/" + youtube_id

    # Create the folder if it doesn't exist
    os.makedirs(output, exist_ok=True)

    image_path = output + "/" + frame_id + ".jpeg"
        
    captured = capture_frame(video_filename, output_image=image_path)
    
    if captured:
        return Image.open(image_path)
    else:
        return False
                
