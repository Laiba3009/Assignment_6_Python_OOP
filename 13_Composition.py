# Engine class
class Engine:
    def start(self):
        return "Engine started"

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine is part of Car

    def start_car(self):
        return self.engine.start()  # Access Engine method via Car

# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car
my_car = Car(my_engine)

# Start the car
print(my_car.start_car())

