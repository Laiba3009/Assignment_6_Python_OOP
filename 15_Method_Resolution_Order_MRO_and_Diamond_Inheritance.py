# Class A with show() method
class A:
    def show(self):
        print("Class A")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("Class B")

# Class C inherits from A and overrides show()
class C(A):
    def show(self):
        print("Class C")

# Class D inherits from both B and C
class D(B, C):
    pass

# Create an object of class D
obj = D()

# Call the show() method
obj.show()

