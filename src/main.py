from fastapi import FastAPI
from routers import book

app = FastAPI()

app.include_router(book.router)

@app.get("/")
def root():
    return {"APP": "FastApi-simple-project"}
