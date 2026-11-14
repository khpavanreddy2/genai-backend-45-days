# Authentication System

correct_username = "pavan"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login Successful! Welcome.")
    else:
        print("Incorrect Password!")
else:
    print("Incorrect Username!")