def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))


def add(a, b):
    return a + b

print(add(5, 3))

def subtract(a, b):
    return a - b

print(subtract(10, 4))

def multiply(a, b):
    return a * b

print(multiply(3, 7))

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(divide(20, 4))
# print(divide(5, 0))

# def calculator():
#     while True:
#         print("Select operation:")
#         print("1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. Exit")

#         choice = input("Enter choice (1/2/3/4/5): ")

#         if choice == '5':
#             print("Exiting the calculator.")
#             break

#         if choice in ['1', '2', '3', '4']:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))

#             if choice == '1':
#                 print(f"{num1} + {num2} = {add(num1, num2)}")
#             elif choice == '2':
#                 print(f"{num1} - {num2} = {subtract(num1, num2)}")
#             elif choice == '3':
#                 print(f"{num1} * {num2} = {multiply(num1, num2)}")
#             elif choice == '4':
#                 print(f"{num1} / {num2} = {divide(num1, num2)}")
#         else:
#             print("Invalid input")

# print("Starting calculator...")
# calculator()


# Lambda

new_add = lambda a, b: a + b
print(new_add(10, 5))


number = range(11)
squared = list(map(lambda x: x**2, number))
print(squared)


even_number = list(filter(lambda x: x % 2 == 0, number))
print(even_number)


# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial_of_5 = factorial(5)
print(factorial_of_5)
factorial_of_0 = factorial(0)
print(factorial_of_0)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci_of_6 = fibonacci(6)
print(fibonacci_of_6)
fibonacci_of_0 = fibonacci(0)
print(fibonacci_of_0)
