class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property # esto es de tipo getter obtiene el valor de salary
    def salary(self):
        return self._salary

    @salary.setter # esto es de tipo setter modifica el valor de salary
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary canno t be negative")
        self._salary = new_salary

    @salary.deleter # esto es de tipo deleter elimina el valor de salary
    def salary(self):
        print(f"The salary of {self.name} has been deleted")
        del self._salary

# Crear instancia de Employee
employee = Employee("Ana", 5000)
print(employee.salary)

# Modificar el salario de forma controlada
employee.salary = 6000
print(employee.salary)

# Intentar establecer un salario negativo
#employee.salary = -1000

# Eliminar el salario usando el deleter
del employee.salary
