x = 10

if x > 5:
    print("x is greater than 5")
    print("still inside if block")
print("outside if block")


if x < 5:
    print("x is less than 5")
else:
    print("x is not less than 5")
    print("still inside else block")
print("outside else block")


x = 15
y = 20

if x > 10 and y > 15:
    print("Both conditions are true")
else:
    print("At least one condition is false")

if x > 10 or y < 15:
    print("At least one condition is true")
else:
    print("Both conditions are false")

if not (x < 10):
    print("x is not less than 10")

is_member = True
age = 15

if is_member:
    if age < 18:
        print("Member is a minor")
    else:
        print("Member is an adult")
else:
    print("Not a member")


numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

for i in range(9):
    print(i)

for i in range(2,9):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print("Found a banana!")
        break # Exit the loop when banana is found
    print(fruit)

x = 0

while x < 5:
    print(x)
    x += 1  # Increment x to avoid infinite loop


numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue  # Skip the rest of the loop when num is 3
    print(num)

# example of iterating

my_list = [10, 20, 30, 40, 50]

my_iterator = iter(my_list)

# using next() to get elements from the iterator
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30
print(next(my_iterator))  # Output: 40
print(next(my_iterator))  # Output: 50

text = "Hello World"

iter_text = iter(text)

# print(next(iter_text))  # Output: H
# print(next(iter_text))  # Output: e
# print(next(iter_text))  # Output: l
# print(next(iter_text))  # Output: l
# print(next(iter_text))  # Output: o
# print(next(iter_text))  # Output:
# print(next(iter_text))  # Output: W
# print(next(iter_text))  # Output: o
# print(next(iter_text))  # Output: r
# print(next(iter_text))  # Output: l
# print(next(iter_text))  # Output: d

for char in iter_text:
    print(char)


# limit

limit = 10

odd_itter = iter(range(1, limit+1, 2)) # Create an iterator for odd numbers up to limit

for odd in odd_itter:
    print(odd)

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


# Fibonacci generator

def fibonacci(n):
    a, b = 0, 1 # Starting values a = 0 and b = 1
    while a < n:
        yield a
        a, b = b, a + b  # Update values to the next Fibonacci numbers

for num in fibonacci(50):
    print(num)


# comprehension list

squares = [x**2 for x in range(1, 11)] # List of squares of numbers from 1 to 10
print(squares)


celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius] # Convert Celsius to Fahrenheit
print(fahrenheit)


evens = [x for x in range(1, 21) if x % 2 == 0] # List of even numbers from 1 to 20
print(evens)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))] # Transpose the 2D matrix

print("Original matrix:")
print(matrix)

print("Transposed matrix:")
print(transposed)

flattened = [num for row in matrix for num in row] # Flatten the 2D matrix into a 1D list
print(flattened)
