from diskcache import Cache

from ..params import TMP_FOLDER

cache = Cache(TMP_FOLDER)

def get_cache(id: str):
    if id in cache:
        return cache[id]

def set_cache(id: str, data, days = 360):
    cache.set(id, data, expire=days * 60 * 60)