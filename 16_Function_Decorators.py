# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()  # Call the original function
    return wrapper

# Function to apply the decorator to
@log_function_call
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

