from contextlib import asynccontextmanager

import uvicorn
from database import create_tables
from routes.reviews import router as review_router

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created")
    yield
    # shutdown: cleanup here
    print("Shutting down the app now")


app = FastAPI(
    title="Theatre Reviews API",
    description="An Api used to create and edit theatre reviews for JJ's Shows",
    lifespan=lifespan,
)

app.include_router(review_router)


@app.get("/")
def root():
    return {"message": "Welcome to JJ's Shows review API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
