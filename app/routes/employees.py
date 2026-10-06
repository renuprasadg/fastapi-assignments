from fastapi import APIRouter, HTTPException
from app.data import sample_data

router = APIRouter()

@router.get("/employees")
def get_employees(location: str|None = None, 
                  role: str|None = None, 
                  min_experience: int|None = None
    ):
    #filter by location
    result = sample_data.employees

    if location:
        result = [
            employee
            for employee in result
            if employee["location"].lower() == location.lower()
        ]
    if role:
        result = [
            employee
            for employee in result
            if employee["role"].lower() == role.lower()
        ]        
    if min_experience is not None:
        result = [
            employee
            for employee in result
            if employee["experience"] >= min_experience
        ]         
    return result   

@router.get("/employess/{employee_id}")
def get_employee_by_id(employee_id: int):
    for employee in sample_data.employees:
        if employee_id == employee['id']:
            return employee
    raise HTTPException( 
        status_code=404, 
        detail="Employee id not found" 
    )     