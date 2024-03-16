from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    """List all employees."""
    employees = Employee.select()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    """Find an employee by name."""
    name = input("Enter the employee's name: ")
    employee = Employee.get_or_none(Employee.name == name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id(employee_id):
    """Find an employee by ID."""
    employee = Employee.get_or_none(Employee.id == employee_id)
    return employee


def create_employee(name, position, department_id):
    """Create a new employee."""
    employee = Employee.create(name=name, position=position, department_id=department_id)
    return employee


def update_employee(employee_id, name=None, position=None, department_id=None):
    """Update an existing employee."""
    employee = find_employee_by_id(employee_id)
    if employee:
        if name:
            employee.name = name
        if position:
            employee.position = position
        if department_id:
            employee.department_id = department_id
        employee.save()
        return employee
    else:
        return None

def delete_employee(employee_id):
    """Delete an existing employee."""
    employee = find_employee_by_id(employee_id)
    if employee:
        employee.delete_instance()
        return True
    else:
        return False

def list_employees_in_department(department_id):
    """List all employees in a department."""
    employees = Employee.select().where(Employee.department_id == department_id)
    for employee in employees:
        print(employee)