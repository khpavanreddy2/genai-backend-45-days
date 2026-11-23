
# DAY 5 - PYTHON COLLECTIONS PRACTICE

# 1. LISTS
numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)

print("List:", numbers)
print("Largest:", max(numbers))
print("Smallest:", min(numbers))


# 2. TUPLES
values = (10, 20, 30, 20, 40, 20, 50)

print("First:", values[0])
print("Last:", values[-1])
print("Count of 20:", values.count(20))
print("Index of 40:", values.index(40))

# Convert tuple to list, add an item, convert back
data = list(values)
data.append(60)
result = tuple(data)

print("Updated tuple:", result)


# 3. SETS
A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)

A.add(80)
A.remove(20)

print("Updated set:", A)


# 4. DICTIONARIES
student = {
    "name": "Pavan",
    "age": 23,
    "skills": ["Python", "SQL", "ML"]
}

student["skills"].append("Generative AI")
student["age"] = 24
student["city"] = "Bengaluru"

print("Student:", student)

for key, value in student.items():
    print(key, ":", value)


# 5. MIXED DATA STRUCTURES
students = [
    {
        "name": "Pavan",
        "marks": [80, 90, 85],
        "skills": {"Python", "SQL"}
    },
    {
        "name": "Rahul",
        "marks": [70, 75, 80],
        "skills": {"Java", "Python"}
    }
]

for student in students:
    total = sum(student["marks"])
    average = total / len(student["marks"])

    print("\nName:", student["name"])
    print("Total:", total)
    print("Average:", average)

# Find common skills
pavan_skills = students[0]["skills"]
rahul_skills = students[1]["skills"]

common_skills = pavan_skills & rahul_skills

print("\nCommon skills:", common_skills)
