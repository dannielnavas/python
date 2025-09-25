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
