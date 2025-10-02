def log_decorator(func):
    def wrapper():
        print('Function is being called')
        func()
        print('Function has been called')
    return wrapper

@log_decorator
def process_payment(amount):
    print(f"Processing payment of ${amount}")

process_payment(100)
