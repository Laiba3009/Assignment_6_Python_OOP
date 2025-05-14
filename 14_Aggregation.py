# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

# Department class using aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has a reference to an existing Employee

    def show_department_info(self):
        return f"Department: {self.dept_name}, {self.employee.get_details()}"

# Create an Employee object independently
emp1 = Employee("Ayesha", 101)

# Create a Department object that aggregates the Employee
dept1 = Department("HR", emp1)

# Show department info
print(dept1.show_department_info())

