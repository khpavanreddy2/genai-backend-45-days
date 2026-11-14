# Day 2 - Python Fundamentals

# 1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 2. Comparison and Logical Operators
print(10 > 5)
print(10 == 5)
print(10 > 5 and 5 > 2)


# 3. Bitwise Operators
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(4 << 2)
print(16 >> 2)


# 4. Membership Operators
numbers = [10, 20, 30]
print(20 in numbers)
print(40 not in numbers)


# 5. Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)


# 6. Nested Conditions
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")