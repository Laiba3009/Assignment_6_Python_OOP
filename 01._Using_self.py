
class Student:
    def __init__(self, name, marks):
        self.name = name        
        self.marks = marks     

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)

# Example usage
student1 = Student("Laiba", 92)
student1.display()
