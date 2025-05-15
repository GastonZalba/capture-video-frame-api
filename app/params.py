import os, tempfile

# used in the cache, and to download temp .webm files
TMP_FOLDER = os.path.join(tempfile.gettempdir(), 'ytdl')

CACHE_MB_MAX_SIZE = 200
CACHE_DAYS_IMG = 30
CACHE_DAYS_JSON = 360