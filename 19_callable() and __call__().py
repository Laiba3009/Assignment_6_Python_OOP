class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    # Make the object callable
    def __call__(self, number):
        return number * self.factor

# Create an object of Multiplier
double = Multiplier(2)

# Test __call__() by calling object like a function
print(double(5))  # Output: 10

# Check if the object is callable
print(callable(double))  # Output: True

