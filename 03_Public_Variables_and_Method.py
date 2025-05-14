
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} car is starting...")

# Instantiate the class
my_car = Car("Toyota")

# Accessing public variable from outside the class
print("Car Brand:", my_car.brand)

# Accessing public method from outside the class
my_car.start()
