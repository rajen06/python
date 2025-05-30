from fastapi import FastAPI, Path, HTTPException, Query
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
    """
    Retrieve all patient records.
    """
    data = load_data()
    return data


@app.get("/patient/{patient_id}")
def get_patient(
    patient_id: str = Path(
        ..., description="The ID of the patient to retrieve", example="P001"
    )
):
    """
    Retrieve a patient's information by their ID.
    """
    data = load_data()
    patient = data.get(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ..., description="Attribute to sort by height , weight or bmi"
    ),
    order: str = Query("asc", description="Order of sorting: asc or desc"),
):
    """
    Sort patients by a specific attribute.
    """

    valid_fields = ["bmi", "height", "weight"]
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f"Invalid sort field. Valid fields are: {valid_fields}"
        )
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order")
    data = load_data()
    if not data:
        raise HTTPException(status_code=404, detail="No patient records found")
    # Sort the patients based on the specified field and order
    sorted_patients = dict(
        sorted(
            data.items(), key=lambda item: item[1][sort_by], reverse=(order == "desc")
        )
    )
    return sorted_patients
