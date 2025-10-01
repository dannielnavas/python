id1: int = 1
id2: int = 2

total: int = id1 + id2
print(total)


def add_employee(id1: int, id2: int) -> int:
    return id1 + id2
print(add_employee(3, 4))


class Employee:
    def __init__(self, id: int, name: str, age: int, salary: float) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def display(self) -> None:
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

emp1 = Employee(1, "Alice", 30, 50000.0)
emp1.display()

from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None

from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)
