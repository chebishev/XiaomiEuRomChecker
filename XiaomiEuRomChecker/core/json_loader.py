import json
from pathlib import Path
from functools import lru_cache

# core/ directory
CORE_DIR = Path(__file__).resolve().parent

JSON_DIR = CORE_DIR / "json"


@lru_cache
def load_json(name: str) -> dict:
    """
    Load a JSON file from core/json by filename.
    Example: load_json("custom_theme.json")
    """
    path = JSON_DIR / name

    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
