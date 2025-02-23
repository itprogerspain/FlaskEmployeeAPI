```markdown
# Employee Flask API

A simple RESTful API built with Flask to manage employee data, supporting CRUD (Create, Read, Update, Delete) 
operations. This project is containerized with Docker for easy deployment.

## Features
- Retrieve a list of all employees
- Fetch details of a specific employee by ID
- Create a new employee
- Update an existing employee's information
- Delete an employee from the list

## Requirements
- **Python**: 3.12 or higher
- **Dependencies**: Listed in `requirements.txt` (Flask)
- **Docker**: Optional, for containerized deployment

## Installation

### Using Python Directly
1. **Clone the repository**:
   ```bash
   git clone https://github.com/itprogerspain/FlaskEmployeeAPI.git
   cd FlaskEmployeeAPI
   ```
2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python app.py
   ```
   - The API will be available at `http://localhost:5000/`.

### Using Docker
1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/itprogerspain/FlaskEmployeeAPI.git
   cd FlaskEmployeeAPI
   ```
2. **Build the Docker image**:
   ```bash
   docker build -t flask-employee-api .
   ```
3. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 flask-employee-api
   ```
   - Access the API at `http://localhost:5000/`.

**Note**: The `.dockerignore` file excludes unnecessary files like `.git`, `.gitignore`, and `*.md` to keep the Docker image lightweight.

## API Endpoints

| Method | Endpoint             | Description                        | Request Body (JSON)                  | Response                                    |
|--------|----------------------|------------------------------------|--------------------------------------|---------------------------------------------|
| GET    | `/`                  | Welcome message                   | None                                 | `"Welcome to the Employee API"`            |
| GET    | `/employees`         | List all employees                | None                                 | JSON array of employees                    |
| GET    | `/employees/<id>`    | Get employee by ID                | None                                 | JSON object or `{"error": "Employee not found"}` (404) |
| POST   | `/employees`         | Create a new employee             | `{"name": "string", "age": int, "salary": int}` | Empty body, 201, `Location` header         |
| PUT    | `/employees/<id>`    | Update an employee                | `{"name": "string", "age": int, "salary": int}` | Updated employee JSON or 404               |
| DELETE | `/employees/<id>`    | Delete an employee                | None                                 | JSON with deleted employee and updated list or 404 |

## Example Usage

### Get all employees
```bash
curl http://localhost:5000/employees
```
**Response**:
```json
[
    {"id": 1, "name": "John", "age": 30, "salary": 5000},
    {"id": 2, "name": "Alice", "age": 25, "salary": 6000}
    // ... other employees
]
```

### Create a new employee
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Eve", "age": 28, "salary": 5500}' http://localhost:5000/employees
```
**Response**: Status 201, header `Location: /employees/11`

### Update an employee
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Eve Updated", "age": 29, "salary": 6000}' http://localhost:5000/employees/11
```
**Response**:
```json
{"id": 11, "name": "Eve Updated", "age": 29, "salary": 6000}
```

### Delete an employee
```bash
curl -X DELETE http://localhost:5000/employees/11
```
**Response**:
```json
{
    "deleted_employee": {"id": 11, "name": "Eve Updated", "age": 29, "salary": 6000},
    "updated_employees": [/* remaining employees */]
}
```

## Project Structure
```
FlaskEmployeeAPI/
├── app.py              # Main Flask application code
├── Dockerfile          # Docker configuration file
├── requirements.txt    # Python dependencies
├── .dockerignore       # Files excluded from Docker image
├── .gitignore         # Files excluded from Git
└── README.md          # Project documentation (this file)
```

## Notes
- The API stores data in memory (not persistent). For production use, consider adding a database.
- Use a WSGI server (e.g., Gunicorn) instead of the Flask development server for production deployments.

## License
This project is open-source and available under the MIT License (add a `LICENSE` file if desired).
```

