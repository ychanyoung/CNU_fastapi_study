from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/{item}")
async def create_item(item: str):
    return {"item": item}