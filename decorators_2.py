def log_decorator(func):
    def wrapper(employee):
        if employee.get('role') != 'admin':
            print("Access denied. Admins only.")
        else:
            print('Function is being called')
            func(employee)
            print('Function has been called')
    return wrapper

@log_decorator
def delete_employee(employee):
    print(f"Employee {employee} has been deleted.")

admin_employee = {'name': 'Alice', 'role': 'admin'}
regular_employee = {'name': 'Bob', 'role': 'user'}

delete_employee(admin_employee)  # Should allow deletion
delete_employee(regular_employee)  # Should deny access
