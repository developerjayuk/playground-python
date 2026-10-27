import uvicorn

from fastapi import FastAPI

app = FastAPI(
    title="Pincode Lookup API",
    description="An API to get data for a read only pincode lookup",
)

@app.get("/")
def root():
    return {"message": "Welcome to the Pincode Lookup API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)