from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from DevOps Portfolio!", "status": "running", "author": "youssraguira"}

@app.get("/health")
def health():
    return {"status": "healthy"}
