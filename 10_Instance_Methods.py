class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable
        self.breed = breed    # Instance variable

    def bark(self):
        print(f"{self.name} says: Woof woof!")

# Create a Dog object
dog1 = Dog("Buddy", "Golden Retriever")

# Call the instance method
dog1.bark()

