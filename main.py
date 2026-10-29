
from fastapi import FastAPI
from routes.routes import router as employee_router

app = FastAPI(
    title="Employee CRUD API",
    description="FastAPI application to manage employee records",
    version="1.0.0"
)

app.include_router(employee_router)


@app.get("/")
def home():
    return {"message": "Employee CRUD API is running"}
