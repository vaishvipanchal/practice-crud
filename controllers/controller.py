
from fastapi import HTTPException, status
from models.model import Employee, EmployeeCreate


# Local in-memory storage (no database)
employees: list[Employee] = []
next_id = 1


# 1. Create Employee
def create_employee(employee_data: EmployeeCreate) -> Employee:
    global next_id

    employee = Employee(
        id=next_id,
        **employee_data.model_dump()
    )

    employees.append(employee)
    next_id += 1

    return employee


# 2. Read All Employees
def get_all_employees() -> list[Employee]:
    return employees


# 3. Read Employee by ID
def get_employee_by_id(employee_id: int) -> Employee:
    for employee in employees:
        if employee.id == employee_id:
            return employee

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


# 4. Update Employee
def update_employee(
    employee_id: int,
    employee_data: EmployeeCreate
) -> Employee:
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            updated_employee = Employee(
                id=employee_id,
                **employee_data.model_dump()
            )

            employees[index] = updated_employee
            return updated_employee

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


# 5. Delete Employee
def delete_employee(employee_id: int) -> None:
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            employees.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )
