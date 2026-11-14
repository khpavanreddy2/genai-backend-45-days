# acc_balance = int(input("Enter balance :"))
# acc_withdraw = int(input("Enter withdrwal amount :"))

# if acc_balance > acc_withdraw:
#     print("Withdrawal successfull")
#     print(f"Remaining balance :{acc_balance-acc_withdraw}")
# else:
#     print("Your Balance is Insuffecent")

acc_balance = int(input("Enter balance: "))
acc_withdraw = int(input("Enter withdrawal amount: "))

if acc_withdraw > 0:

    if acc_balance >= acc_withdraw:
        print("Withdrawal successful!")
        remaining = acc_balance - acc_withdraw
        print(f"Remaining balance: {remaining}")

    else:
        print("Insufficient balance")

else:
    print("Invalid withdrawal amount")
