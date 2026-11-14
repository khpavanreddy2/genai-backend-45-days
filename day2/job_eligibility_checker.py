# Job Eligibility Checker

age = int(input("Enter your age: "))
qualification = input("Do you have a degree? (yes/no): ")

if age >= 18:
    if qualification.strip().lower() == "yes":
        print("You are eligible for the job!")
    else:
        print("You need a degree to apply.")
else:
    print("You must be at least 18 years old.")