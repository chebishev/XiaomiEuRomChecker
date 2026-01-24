import json
from functools import lru_cache
from pathlib import Path

import requests

# core/ directory
CORE_DIR = Path(__file__).resolve().parent
JSON_DIR = CORE_DIR / "json"

# Only files that should be fetched from GitHub:
REMOTE_URLS = {
    "HyperOS 3.0.json": "https://raw.githubusercontent.com/chebishev/xiaomi.eu-weekly-roms-checker/main/HyperOS%203.0.json",
}

@lru_cache
def load_json(name: str) -> dict:
    """
    Load a JSON file.
    • Local files load normally
    • Remote files try GitHub first, then fall back to local
    • Remote fetch success → also write local backup
    """

    local_path = JSON_DIR / name

    # 1️⃣ Non-remote JSON → load local only
    if name not in REMOTE_URLS:
        try:
            with open(local_path, encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    # 2️⃣ Try remote fetch
    try:
        url = REMOTE_URLS[name]
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # 2a️⃣ Save remote data to local disk (failsafe backup)
        try:
            JSON_DIR.mkdir(parents=True, exist_ok=True)
            local_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception:
            # Do not break if writing fails
            pass

        return data

    except Exception:
        # Remote failed → fallback to local
        pass

    # 3️⃣ Local fallback
    try:
        with open(local_path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
