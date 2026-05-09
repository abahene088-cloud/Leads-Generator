from fastapi import FastAPI
import os

app = FastAPI(title="Leads Generator")

@app.get("/")
def home():
    return {
        "status": "running",
        "env": os.getenv("APP_ENV", "not set")
    }
