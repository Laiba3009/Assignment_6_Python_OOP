class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # Getter using @property
    @property
    def price(self):
        return self._price

    # Setter using @price.setter
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # Deleter using @price.deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create a Product object
p = Product(100)

# Access price
print("Initial Price:", p.price)

# Update price
p.price = 150
print("Updated Price:", p.price)

# Try setting a negative price
p.price = -20  # Should show warning

# Delete price
del p.price

