from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


app = FastAPI()


class CreatePatient(BaseModel):

    id: Annotated[str, Field(..., description="iD of the patinet", example="P001")]
    name: Annotated[str, Field(..., description="Name of the  Patient")]
    city: Annotated[str, Field(..., description="City of the Patient")]
    age: Annotated[int, Field(..., gt=0, lt=120, desription="Age of the Patient")]
    gender: Annotated[
        Literal["male", "female", "others"],
        Field(..., description="Gender of the Patient"),
    ]
    height: Annotated[
        float, Field(..., gt=0, description="Height of the Patient in meters")
    ]
    weight: Annotated[
        float, Field(..., gt=0, description="Weight of the Patient in kgs")
    ]

    @computed_field
    @property
    def bmi(self) -> float:

        bmi = round(self.weight / (self.height**2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 24.9:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class Updatepatient(BaseModel):

    name: Annotated[Optional[str], Field(default=None, description="Name of the Patient")]
    city: Annotated[Optional[str], Field(default=None, description="City of the Patient")]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120, desription="Age of the Patient")]
    gender: Annotated[
        Optional[Literal["male", "female", "others"]],
        Field(default=None, description="Gender of the Patient"),
    ]
    height: Annotated[
        Optional[float], Field(default=None, gt=0, description="Height of the Patient in meters")
    ]
    weight: Annotated[
        Optional[float], Field(default=None, gt=0, description="Weight of the Patient in kgs")
    ]


def load_data():
    with open("patients.json", "r") as file:
        return json.load(file)


def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)


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
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {valid_fields}",
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


@app.post("/create")
def create_patient(patient: CreatePatient):
    """
    Create a new patient record.
    """
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient ID already exists")

    data[patient.id] = patient.model_dump(exclude=["id"])
    save_data(data)
    return JSONResponse(
        status_code=201, content={"message": "Patient created successfully"}
    )


@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient: Updatepatient):
    """
    Update an existing patient record.
    """
    existing_data = load_data()
    if patient_id not in existing_data:
        raise HTTPException(status_code=404, detail="Patient not found")
    existing_patient = existing_data[patient_id]

    data_to_update = patient.model_dump(exclude_unset=True)

    for key, value in data_to_update.items():
            existing_patient[key] = value

    existing_patient["id"] = patient_id
    patient_pydantic_object = CreatePatient(**existing_patient)
    existing_patient = patient_pydantic_object.model_dump(exclude=["id"])

    existing_data[patient_id] = existing_patient
    save_data(existing_data)
    return JSONResponse(
        status_code=200, content={"message": "Patient updated successfully"}
    )

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    """
    Delete a patient record by ID.
    """
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    del data[patient_id]
    save_data(data)
    return JSONResponse(
        status_code=200, content={"message": "Patient deleted successfully"}
    )
