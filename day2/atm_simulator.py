# ATM Simulator

balance = 10000

print("Welcome to ATM")
print("Available Balance:", balance)

withdraw = int(input("Enter withdrawal amount: "))

if withdraw > 0:
    if balance >= withdraw:
        balance -= withdraw
        print("Withdrawal Successful!")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance!")
else:
    print("Invalid Withdrawal Amount!")