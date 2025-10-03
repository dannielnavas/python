def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


info = print_info(name="Alice", age=30, city="New York")
print(info)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
