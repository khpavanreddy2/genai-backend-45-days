# Student Grade Calculator

marks = int(input("Enter your marks: "))

if 0 <= marks <= 100:

    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")

else:
    print("Invalid marks! Enter marks between 0 and 100.")