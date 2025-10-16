import os
import json
from pathlib import Path
from functools import lru_cache
from uuid import uuid4
from typing import Union

PROJECT_ROOT = Path("/app").resolve()

def base_path(*parts: Union[str, os.PathLike, None]) -> str:
    cleaned = [str(p) for p in parts if p]  # drops None/""
    return str((PROJECT_ROOT.joinpath(*cleaned)).resolve())

def env(name, default=None, *, cast=str):
    val = os.getenv(name, None)
    if val is None:
        return default
    if cast is bool:
        return val.lower() in {"1", "true", "t", "yes", "y", "on"}
    if cast is int:
        try:
            return int(val)
        except ValueError:
            return default
    if cast is list:
        return [x.strip() for x in val.split(",") if x.strip()]
    if cast is dict:
        try:
            return json.loads(val)
        except Exception:
            return default
    return val

def generate_idempotency_key():
    return uuid4().hex  # 32 chars
