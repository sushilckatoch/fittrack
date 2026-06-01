from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FitTrack ML API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
