class Circle:

    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius**2

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

circle = Circle(5)
print(circle.radius)
print(circle.diameter)
print(circle.area)

circle.radius = 10
print(circle.radius)
print(circle.diameter)
print(circle.area)
# circle.radius = -5  # This will raise a ValueError
# print(circle.radius)
