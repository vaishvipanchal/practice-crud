# Employee CRUD API

## Project Description
This project is a REST API developed using FastAPI to perform CRUD (Create, Read, Update, Delete) operations on employee records.

The application uses in-memory storage to manage employee data.

## Technologies Used
- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Git and GitHub
- GitHub Actions (CI/CD)
- Render (Deployment)

## Project Structure
```text
employee-crud/
│
├── controllers/
│   └── controller.py
│
├── models/
│   └── model.py
│
├── routes/
│   └── routes.py
│
├── main.py
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/employees` | Create an employee |
| GET | `/employees` | Retrieve all employees |
| GET | `/employees/{id}` | Retrieve an employee by ID |
| PUT | `/employees/{id}` | Update employee details |
| DELETE | `/employees/{id}` | Delete an employee |

## Employee Fields
- ID
- Name
- Email
- Department
- Salary

## Installation and Execution

1. Clone the repository:
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project folder:
```bash
cd employee-crud
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn main:app --reload
```

5. Open the API documentation:
```text
http://127.0.0.1:8000/docs
```

## CI/CD Pipeline
GitHub Actions is used to automate the build and validation process whenever code is pushed to or a pull request is created for the `main` branch.

## Deployment
The application is deployed using Render.

## Note
Employee records are stored in memory and may be lost when the application restarts.
