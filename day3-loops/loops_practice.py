"""
Day 03 – Python Loops Practice
Topics: for, range, while, break, continue, pass, nested loops,
accumulators, and star patterns.
"""

# 1. for loop with range()
print("1. Numbers from 0 to 4")
for i in range(5):
    print(i)

# 2. range(start, stop)
print("\n2. Numbers from 2 to 5")
for i in range(2, 6):
    print(i)

# 3. range(start, stop, step)
print("\n3. Odd numbers from 1 to 9")
for i in range(1, 10, 2):
    print(i)

# 4. Counting backward
print("\n4. Countdown")
for i in range(5, 0, -1):
    print(i)

# 5. while loop
print("\n5. while loop")
count = 1
while count <= 5:
    print(count)
    count += 1

# 6. break: stop the loop
print("\n6. break example")
for i in range(1, 8):
    if i == 5:
        break
    print(i)

# 7. continue: skip the current iteration
print("\n7. continue example")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 8. pass: placeholder statement
print("\n8. pass example")
for _ in range(3):
    pass

# 9. Accumulator: sum numbers from 1 to 4
print("\n9. Sum using an accumulator")
total = 0
for i in range(1, 5):
    total += i
print("Total:", total)

# 10. Nested loops
print("\n10. Nested loop: 3 rows and 2 columns")
for row in range(1, 4):
    for col in range(1, 3):
        print(f"row={row}, col={col}")

# 11. Right triangle pattern
print("\n11. Right triangle")
for row in range(1, 5):
    for col in range(row):
        print("*", end=" ")
    print()

# 12. Inverted triangle pattern
print("\n12. Inverted triangle")
for row in range(4, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()
