from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"message": f"Item {item_id}"}


    