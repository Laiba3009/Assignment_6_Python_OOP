
class Counter:
    count = 0  # Class variable to track number of objects

    def __init__(self):
        Counter.count += 1  # Increase count each time an object is created

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)


# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.show_count()  # Output: Total objects created: 3
