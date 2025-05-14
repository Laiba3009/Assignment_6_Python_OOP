# Step 1: Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        self.message = message
        super().__init__(self.message)

# Step 2: Define a function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise custom exception
    else:
        print("Access granted.")

# Step 3: Use try...except to handle it
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Error:", e)

