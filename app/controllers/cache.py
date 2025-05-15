from diskcache import Cache

from ..params import tmp_folder

cache = Cache(tmp_folder)

def get_cache(id: str):
    if id in cache:
        return cache[id]

def set_cache(id: str, data, days = 360):
    cache.set(id, data, expire=days * 60 * 60)