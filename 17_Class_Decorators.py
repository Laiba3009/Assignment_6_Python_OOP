# Class decorator
def add_greeting(cls):
    # Add a new method to the class
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Attach the method to the class
    return cls  # Return the modified class

# Apply decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create object and call the new method
p = Person("Laiba")
print(p.greet())  # Calling the method added by the decorator

