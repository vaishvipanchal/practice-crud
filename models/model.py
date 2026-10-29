
from pydantic import BaseModel, EmailStr, Field


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    department: str = Field(..., min_length=2, max_length=100)
    salary: float = Field(..., gt=0)


class Employee(EmployeeCreate):
    id: int = Field(..., gt=0)
