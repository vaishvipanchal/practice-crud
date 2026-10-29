
from fastapi import APIRouter, status
from models.model import Employee, EmployeeCreate
from controllers import controller  as employee_controller

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# 1. Create Employee
@router.post(
    "",
    response_model=Employee,
    status_code=status.HTTP_201_CREATED
)
def create_employee(employee: EmployeeCreate):
    return employee_controller.create_employee(employee)


# 2. Read All Employees
@router.get(
    "",
    response_model=list[Employee]
)
def get_all_employees():
    return employee_controller.get_all_employees()


# 3. Read Employee by ID
@router.get(
    "/{employee_id}",
    response_model=Employee
)
def get_employee(employee_id: int):
    return employee_controller.get_employee_by_id(employee_id)


# 4. Update Employee
@router.put(
    "/{employee_id}",
    response_model=Employee
)
def update_employee(
    employee_id: int,
    employee: EmployeeCreate
):
    return employee_controller.update_employee(
        employee_id,
        employee
    )


# 5. Delete Employee
@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_employee(employee_id: int):
    employee_controller.delete_employee(employee_id)
    return None
