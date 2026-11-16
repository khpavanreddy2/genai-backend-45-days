"""
Day 03 – Number Problems Using Loops
Practice with factorial, digits, reverse, palindrome, Armstrong,
largest/smallest digit, and even/odd digit counts.
"""

# 1. Factorial
num = int(input("Enter a non-negative integer for factorial: "))
if num < 0:
    print("Factorial is not defined for negative integers.")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial:", fact)


# 2. Count digits (works for zero and negative inputs)
num = abs(int(input("\nEnter a number to count its digits: ")))
if num == 0:
    digit_count = 1
else:
    digit_count = 0
    temp = num
    while temp > 0:
        digit_count += 1
        temp //= 10
print("Digit count:", digit_count)


# 3. Sum of digits
num = abs(int(input("\nEnter a number to find the sum of its digits: ")))
total = 0
temp = num
while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10
print("Sum of digits:", total)


# 4. Reverse a number (preserves a negative sign)
num = int(input("\nEnter a number to reverse: "))
sign = -1 if num < 0 else 1
temp = abs(num)
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("Reversed number:", sign * reverse)


# 5. Palindrome check (non-negative integers)
num = int(input("\nEnter a non-negative number for palindrome check: "))
original = num
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if original >= 0 and original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")


# 6. Armstrong number check
num = int(input("\nEnter a non-negative number for Armstrong check: "))
original = num
temp = num
power = len(str(temp))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if original >= 0 and total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# 7. Largest and smallest digit
num = abs(int(input("\nEnter a number to find largest and smallest digits: ")))
if num == 0:
    largest = smallest = 0
else:
    largest = 0
    smallest = 9
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        temp //= 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)


# 8. Count even and odd digits
num = abs(int(input("\nEnter a number to count even and odd digits: ")))
even_count = 0
odd_count = 0

if num == 0:
    even_count = 1
else:
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        temp //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)
