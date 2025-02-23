# Import necessary libraries for JSON handling and Flask framework
import json
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Define the homepage route
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Employee API"

# Sample list of employees (in-memory storage)
employees = [{'id': 1, 'name': 'John', 'age': 30, 'salary': 5000}, 
             {'id': 2, 'name': 'Alice', 'age': 25, 'salary': 6000}, 
             {'id': 3, 'name': 'Bob', 'age': 40, 'salary': 7200},
             {'id': 4, 'name': 'Charlie', 'age': 35, 'salary': 8300},
             {'id': 5, 'name': 'David', 'age': 45, 'salary': 8000},
             {'id': 6, 'name': 'Julian', 'age': 50, 'salary': 9000},
             {'id': 7, 'name': 'Helen', 'age': 44, 'salary': 6500},
             {'id': 8, 'name': 'Jorje', 'age': 34, 'salary': 7500},
             {'id': 9, 'name': 'Alex', 'age': 43, 'salary': 8200},
             {'id': 10, 'name': 'Luis', 'age': 38, 'salary': 7000}]


# Variable to track the next available employee ID
nextEmployeeId = 11

# Route to get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    """Return a JSON list of all employees."""
    return jsonify(employees)


# Route to get a specific employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    """Retrieve an employee by their ID from the list.

        Args:
            id (int): The unique identifier of the employee to fetch.

        Returns:
            jsonify: A JSON response containing the employee data if found,
                     or an error message with status 404 if not found.
        """
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify(employee)


# Route to get a specific employee by ID
def get_employee(id):
    """Search for an employee in the list by ID. Return None if not found."""
    for employee in employees:
        if employee['id'] == id:
            return employee
    return None


# Helper function to validate employee data
def employee_is_valid(employee):
    """Check if the employee data contains only valid properties."""
    for key in employee.keys():
        if key not in ['id', 'name', 'age', 'salary']:
            return False
    return True
    

# Route to create a new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    """Add a new employee to the list. Assign a new ID and return the location."""
    global nextEmployeeId
    employee = json.loads(request.data)
    if not employee_is_valid(employee):
        return jsonify({'error': 'Invalid employee properties'}), 400
    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)
    return '', 201, {'Location': f'/employees/{employee["id"]}'}


# Route to update an existing employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
    """Update an employee's details by ID. Return 404 if not found."""
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    updated_employee = json.loads(request.data)
    if not employee_is_valid(updated_employee):
        return jsonify({'error': 'Invalid employee properties'}), 400
    employee.update(updated_employee)
    return jsonify(employee)


# Route to delete an employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    """Remove an employee by ID. Return 404 if not found, otherwise return deleted data."""
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    employees.remove(employee)  
    return jsonify({
        'deleted_employee': employee,  
        'updated_employees': employees  
    }), 200  


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    """Start the Flask development server on port 5000 with debug mode enabled."""
    app.run(debug=True, host='0.0.0.0', port=5000)