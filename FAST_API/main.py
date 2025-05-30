from fastapi import FastAPI
import json


app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        return json.load(file)
    
@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def get_item():
    return {"message": "A fully functional API to manage patients records"}


@app.get("/view")
def view():
    data = load_data()
    return data
