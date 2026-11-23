
# DAY 6 - PYTHON FUNCTIONS
# 45-Day Junior GenAI Engineer Program


# 1. BASIC FUNCTION

def introduce():
    print("My name is Pavan")
    print("I am learning Python")
    print("My goal is to become a GenAI Engineer")


introduce()


# 2. PARAMETERS AND ARGUMENTS

def student_details(name, age):
    print(f"My name is {name}")
    print(f"My age is {age}")


student_details("Pavan", 23)


# 3. RETURN STATEMENT

def calculate_square(number):
    square = number * number
    return square


result = calculate_square(5)
print("Square:", result)


# 4. DEFAULT ARGUMENTS

def calculate_bill(price, quantity=1):
    return price * quantity


print("Bill 1:", calculate_bill(100))
print("Bill 2:", calculate_bill(100, 3))


# 5. POSITIONAL AND KEYWORD ARGUMENTS

def employee(name, salary, city):
    print(name, salary, city)


employee("Pavan", 30000, "Bengaluru")

employee(
    salary=30000,
    city="Bengaluru",
    name="Pavan"
)


# 6. LOCAL AND GLOBAL VARIABLES

balance = 1000

def deposit(amount):
    global balance
    balance += amount


deposit(500)
print("Updated balance:", balance)


# 7. *ARGS

def calculate_total(*numbers):
    total = sum(numbers)
    return total


print("Total 1:", calculate_total(10, 20, 30))
print("Total 2:", calculate_total(5, 10, 15, 20, 25))


# 8. **KWARGS

def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

    return kwargs


employee_details(
    name="Pavan",
    salary=30000,
    city="Bengaluru",
    role="GenAI Engineer"
)


# 9. LAMBDA FUNCTIONS

square = lambda number: number * number
print("Square:", square(5))

add = lambda a, b: a + b
print("Addition:", add(10, 20))

check = lambda number: "Even" if number % 2 == 0 else "Odd"
print(check(10))
print(check(7))

maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(25, 40))


# 10. STUDENT RESULT CALCULATOR

def student_result(name, *marks):
    if not marks:
        return {
            "name": name,
            "total": 0,
            "average": 0
        }

    total = sum(marks)
    avg = total / len(marks)

    student = {
        "name": name,
        "total": total,
        "average": avg
    }

    return student


result = student_result("Pavan", 80, 90, 85)
print("Student Result:", result)


# 11. PRODUCT DETAILS

def product_details(**items):
    for key, value in items.items():
        print(key, ":", value)

    return items


product_details(
    name="Laptop",
    price=55000,
    brand="HP",
    warranty="2 years"
)


# 12. DISCOUNT CALCULATOR

def calculate_discount(price, discount=10):
    discount_amount = (price * discount) / 100
    return price - discount_amount


print("Discounted Price:", calculate_discount(1000))

print(
    "Discounted Price:",
    calculate_discount(price=2000, discount=20)
)


# 13. EMPLOYEE SALARY CALCULATOR

def employee_salary(
    name,
    salary,
    bonus=5000,
    *additional_deduction,
    **employee_details
):
    total_deduction = sum(additional_deduction)

    final_salary = salary + bonus - total_deduction

    employee = {
        "name": name,
        "final_salary": final_salary,
        "city": employee_details.get("city"),
        "role": employee_details.get("role")
    }

    return employee


result = employee_salary(
    "Pavan",
    30000,
    5000,
    1000,
    500,
    city="Bengaluru",
    role="GenAI Engineer"
)

print("Employee Salary:", result)
