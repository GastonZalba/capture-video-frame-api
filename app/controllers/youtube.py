from yt_dlp import YoutubeDL
from yt_dlp.utils import download_range_func

def create_url(youtube_id: str):
    return "https://www.youtube.com/watch?v=" + youtube_id

def download_youtube_video(youtube_id, start_seconds, video_filename, resolution):
    ydl_opts = {
        "verbose": False,
        "format": f"bv[height={resolution}][vcodec^=avc1]/bv[vcodec^=avc1]",
        "outtmpl": video_filename,
        "download_ranges": download_range_func(None, [(start_seconds, start_seconds + 0.1)]),
        "force_keyframes_at_cuts": True,
        "allow_multiple_video_streams": False,
        "allow_multiple_audio_streams": False,
        "concurrent_fragment_downloads": 1,
        "force_generic_extractor": False,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([create_url(youtube_id)])

def get_youtube_qualities(youtube_id: str):
        
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'no_warnings': True
    }
    
    results = []

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(create_url(youtube_id), download=False)

        for fmt in info['formats']:
            if fmt.get('vcodec') != 'none' and fmt.get('acodec') == 'none':  # Solo video (sin audio)
                height = fmt.get('height')
                resolution = height if height else 'unknown'
                fps = fmt.get('fps') or 'unknown'
                kbps = int(fmt.get('tbr')) if fmt.get('tbr') else 'unknown'
                code = fmt.get('format_id')

                results.append({
                    'code': code,
                    'resolution': resolution,
                    'fps': fps,
                    'kbps': kbps
                })
        
    return results