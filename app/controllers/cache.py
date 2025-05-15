from diskcache import Cache

from ..params import TMP_FOLDER, CACHE_MB_MAX_SIZE 

cache = Cache(TMP_FOLDER, size_limit=CACHE_MB_MAX_SIZE * 1024**2)

def get_cache(id: str):
    if id in cache:
        return cache[id]

def set_cache(id: str, data, days = 360):
    cache.set(id, data, expire=days * 60 * 60)