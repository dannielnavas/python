def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            if employee.get('role') != required_role:
                print(f"Access denied. {required_role.capitalize()}s only.")
            else:
                print('Function is being called')
                func(employee)
                print('Function has been called')
        return wrapper
    return decorator
def log_action(func):
    def wrapper(employee):
        print('Action is being logged')
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f"Employee {employee} has been deleted.")

admin_employee = {'name': 'Alice', 'role': 'admin'}
regular_employee = {'name': 'Bob', 'role': 'user'}
delete_employee(admin_employee)  # Should allow deletion
delete_employee(regular_employee)  # Should deny access
