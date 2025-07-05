from fastapi import FastAPI, Header, HTTPException
import os

app = FastAPI()

def check_api_key(x_api_key: str = Header(default=None)):
    if x_api_key != "your-secure-api-key":
        raise HTTPException(status_code=403, detail="Forbidden")

@app.get("/moonshot")
def moonshot(x_api_key: str = Header(default=None)):
    check_api_key(x_api_key)
    return {"status": "ok", "action": "moonshot activated"}

@app.get("/rotation")
def rotation(x_api_key: str = Header(default=None)):
    check_api_key(x_api_key)
    return {"status": "ok", "action": "rotation strategy"}

@app.get("/risk")
def risk(x_api_key: str = Header(default=None)):
    check_api_key(x_api_key)
    return {"status": "ok", "risk_level": "moderate"}

@app.get("/evaluate")
def evaluate(x_api_key: str = Header(default=None)):
    check_api_key(x_api_key)
    return {"status": "ok", "evaluation": "success"}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("exo_fin_gpt.exo_interface_api.exo_interface_api:app", host="0.0.0.0", port=port)
