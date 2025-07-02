
from fastapi import FastAPI
from pydantic import BaseModel
from data_store import save_log, load_logs

app = FastAPI()

class WaterEntry(BaseModel):
    amount_ml: int

@app.post("/log/")
async def log_water(entry: WaterEntry):
    save_log(entry.amount_ml)
    return {"message": f"{entry.amount_ml} ml logged successfully."}

@app.get("/logs/")
async def get_logs():
    return load_logs()
