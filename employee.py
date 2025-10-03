class Employee:
    def __init__(self, name: str, *args, **kwargs) -> None:
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self) -> None:
        print(f"Employee Name: {self.name}")
        print(f"Skills: {self.skills}")
        print(f"Details: {self.details}")

emp = Employee("Alice", "Python", "Django", age=30, department="IT")
emp.show_employee()
