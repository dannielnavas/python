def divide_numbers(numerator: int, denominator: int) -> float:
    """Divide two numbers and return the result.

    Args:
        numerator (int): The numerator.
        denominator (int): The denominator.

    Returns:
        float: The result of the division.
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        # print("Both numerator and denominator must be integers.")
        # return None
        raise TypeError("Both numerator and denominator must be integers.")
    if denominator == 0:
        # print("Error: Division by zero is not allowed.")
        # return None
        raise ValueError("Denominator cannot be zero.")

    return numerator // denominator


# result = divide_numbers(10, 2)
# print(f"Resultado de la división: {result}")
# result = divide_numbers(10, 0)
# print(f"Resultado de la división: {result}")
# result = divide_numbers(10, 'a')
# print(f"Resultado de la división: {result}")

try:
    result = divide_numbers(10, 0)
    print(f"Resultado de la división: {result}")
except ValueError as ve:
    print(f"ValueError: {ve}")
except TypeError as te:
    print(f"TypeError: {te}")
