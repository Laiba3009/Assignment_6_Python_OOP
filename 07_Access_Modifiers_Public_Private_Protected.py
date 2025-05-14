
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn            # Private variable

# Create an object of Employee
emp = Employee("Laiba", 50000, "123-45-6789")

# Accessing public variable
print("Public - Name:", emp.name)

# Accessing protected variable
print("Protected - Salary:", emp._salary)

# Trying to access private variable
try:
    print("Private - SSN:", emp.__ssn)
except AttributeError as e:
    print("Private - SSN: Cannot access directly:", e)

# Accessing private variable using name mangling
print("Private - SSN (via name mangling):", emp._Employee__ssn)
