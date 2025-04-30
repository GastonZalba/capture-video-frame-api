import yt_dlp
from yt_dlp.utils import download_range_func

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
