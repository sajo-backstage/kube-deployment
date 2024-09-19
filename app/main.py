from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello World"})

@app.get("/sample")
def sampleroute():
    return {"message": "Sample Route"}

@app.get("/python")
def python():
    return "Hello, Python!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
