from fastapi import FastAPI

app = FastAPI(title="LeadFlow AI")

@app.get("/")
def home():
    return {"status": "LeadFlow AI backend running"}
