
# Day 6 – Python Functions

## Topics Covered
1. What are functions?
2. Creating and calling functions
3. Parameters and arguments
4. Return statement
5. Default arguments
6. Positional and keyword arguments
7. Local and global variables
8. Variable-length arguments (*args)
9. Keyword variable-length arguments (**kwargs)
10. Lambda functions
11. Practical function exercises

---

## 1. What is a Function?

A function is a reusable block of code that performs a particular task.

Functions help us:
- Reuse code.
- Avoid repetition.
- Organize programs.
- Make code easier to understand and maintain.

### Creating a Function

```python
def greet():
    print("Hello Pavan!")

greet()
```

- `def` is used to define a function.
- `greet` is the function name.
- `greet()` calls the function.
- Function code executes when the function is called.

---

## 2. Parameters and Arguments

Parameters are variables defined in a function.
Arguments are actual values passed when calling a function.

```python
def greet(name):
    print("Hello", name)

greet("Pavan")
```

- `name` is a parameter.
- `"Pavan"` is an argument.

Functions can accept multiple parameters.

```python
def student_details(name, age):
    print(f"My name is {name}")
    print(f"My age is {age}")

student_details("Pavan", 23)
```

---

## 3. Return Statement

The return statement sends a value back from a function.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:
30

### Print vs Return

- `print()` displays information on the screen.
- `return` sends a value back to the caller.
- A function without an explicit return statement returns `None`.

---

## 4. Default Arguments

Default arguments provide a value when the caller does not supply one.

```python
def calculate_bill(price, quantity=1):
    return price * quantity

print(calculate_bill(100))
print(calculate_bill(100, 3))
```

Output:
100
300

The default quantity is 1, but the caller can override it.

---

## 5. Positional and Keyword Arguments

### Positional Arguments

Values are assigned according to their position.

```python
def employee(name, salary, city):
    print(name, salary, city)

employee("Pavan", 30000, "Bengaluru")
```

### Keyword Arguments

Values are assigned using parameter names.

```python
employee(city="Bengaluru", salary=30000, name="Pavan")
```

Important:
- Positional arguments must come before keyword arguments.
- Keyword arguments can be supplied in a different order.

---

## 6. Local and Global Variables

### Local Variable

A variable created inside a function.

```python
def greet():
    message = "Hello Pavan"
    print(message)

greet()
```

A local variable is normally accessible only inside its function.

### Global Variable

A variable created outside a function.

```python
name = "Pavan"

def greet():
    print(name)

greet()
```

### Global Keyword

The global keyword allows a function to reassign a global variable.

```python
balance = 1000

def deposit(amount):
    global balance
    balance += amount

deposit(500)
print(balance)
```

Output:
1500

---

## 7. Variable-Length Arguments – *args

`*args` allows a function to accept any number of positional arguments.

The arguments are collected into a tuple.

```python
def calculate_total(*numbers):
    return sum(numbers)

print(calculate_total(10, 20, 30))
print(calculate_total(5, 10, 15, 20, 25))
```

Output:
60
75

---

## 8. Keyword Variable-Length Arguments – **kwargs

`**kwargs` allows a function to accept any number of keyword arguments.

The arguments are collected into a dictionary.

```python
def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_details(
    name="Pavan",
    salary=30000,
    city="Bengaluru"
)
```

### Difference Between *args and **kwargs

| Feature | *args | **kwargs |
|---|---|---|
| Accepts | Positional arguments | Keyword arguments |
| Stores as | Tuple | Dictionary |
| Example | 10, 20, 30 | name="Pavan" |

---

## 9. Lambda Functions

A lambda function is a small anonymous function written in one expression.

Syntax:

```python
lambda arguments: expression
```

Normal function:

```python
def square(number):
    return number * number
```

Lambda function:

```python
square = lambda number: number * number

print(square(5))
```

Lambda with multiple arguments:

```python
add = lambda a, b: a + b
print(add(10, 20))
```

Lambda with condition:

```python
check = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check(10))
print(check(7))
```

Important:
- Lambda automatically returns its expression's result.
- Explicit return is not needed.
- Best suited for small, simple expressions.

---

## 10. Practical Exercises Completed

### Exercise 1 – Student Result Calculator

- Accept student name and multiple marks.
- Calculate total and average.
- Return results in a dictionary.

### Exercise 2 – Product Details

- Accept multiple keyword arguments using **kwargs.
- Print each key and value.
- Return the dictionary.

### Exercise 3 – Discount Calculator

- Accept price and default discount.
- Calculate discount amount.
- Return final price.

### Exercise 4 – Employee Salary Calculator

- Accept employee name and salary.
- Use default bonus.
- Accept multiple deductions using *args.
- Accept additional employee details using **kwargs.
- Return final salary and employee information.

---

## Important Interview Questions

1. What is a function in Python?
2. Difference between parameters and arguments?
3. Difference between print() and return?
4. What are default arguments?
5. Difference between positional and keyword arguments?
6. Difference between local and global variables?
7. What is the global keyword?
8. Difference between *args and **kwargs?
9. What is a lambda function?
10. What happens when a function has no return statement?
11. Can a function return multiple values?
12. What are mutable default arguments and why should they be avoided?

---

## Day 6 – Completion Status

Completed:
- Function creation and calling
- Parameters and arguments
- Return statement
- Default arguments
- Positional and keyword arguments
- Local and global variables
- *args and **kwargs
- Lambda functions
- Practical coding exercises
- Interview preparation

**Day 6 Status: Completed**
