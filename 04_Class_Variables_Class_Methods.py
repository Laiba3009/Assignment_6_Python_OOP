
class Bank:
    bank_name = "Laiba Bank"  # Class variable

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change the class variable using cls

    def show_details(self):
        print(f"Customer: {self.customer_name}, Bank: {self.bank_name}")


# Creating instances
acc1 = Bank("Maryam")
acc2 = Bank("Hira")

# Show initial bank names
acc1.show_details()  # Output: Customer: Alice, Bank: Default Bank
acc2.show_details()  # Output: Customer: Bob, Bank: Default Bank

# Change bank name using class method
Bank.change_bank_name("Global Trust Bank")

# Show updated bank names (should reflect in all instances)
acc1.show_details()  # Output: Customer: Alice, Bank: Global Trust Bank
acc2.show_details()  # Output: Customer: Bob, Bank: Global Trust Bank
