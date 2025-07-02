
import json
from datetime import datetime
import os

DATA_FILE = "data/water_logs.json"

def ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")

def load_logs():
    ensure_data_dir()
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_log(amount_ml):
    ensure_data_dir()
    logs = load_logs()
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "amount_ml": amount_ml
    })
    with open(DATA_FILE, "w") as f:
        json.dump(logs, f, indent=2)
