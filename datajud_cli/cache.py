import diskcache
import os
from pathlib import Path

CACHE_DIR = Path.home() / ".datajud" / "cache"
CACHE_TTL = 60 * 60 * 24 # 24 horas em segundos

def get_cache() -> diskcache.Cache:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return diskcache.Cache(str(CACHE_DIR))

def cache_key(numero: str, trubinal: str) -> str:
    return f"{trubinal}:{numero}"

def get_cached(numero: str, trubinal: str) -> dict | None:
    with get_cache() as cache:
        return cache.get(cache_key(numero, trubinal))
    
def set_cached(numero: str, trubinal: str, data: dict) -> None:
    with get_cache() as cache:
        cache.set(cache_key(numero, trubinal), data, expire=CACHE_TTL)