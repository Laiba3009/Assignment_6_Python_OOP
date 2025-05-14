# Base class
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject

# Create an object of Teacher
teacher = Teacher("Sir Asharib", "Python")

# Display information
print("Name:", teacher.name)
print("Subject:", teacher.subject)

