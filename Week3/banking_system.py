try:
    name=input("Enter the Name: ")
    age=int(input("Enter the Age: "))
    balance=float(input("Enter the Account Balance: "))
    withdrawal_amount=float(input("Enter the Withdrawl Amount: "))
    if age<18:
        raise ValueError("Customer must be at least 18 years old.")
    if balance<0:
        raise ValueError("Balance cannot be negative.")
    if withdrawal_amount<0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if withdrawal_amount>balance:
        raise ValueError("Insufficient balance.")

except ValueError as e:
    print(e)

else:
    print("Transaction successfull")
    print(f"Customer : {name}")
    print(f"Remaining Balance : {balance-withdrawal_amount}")

finally:
    print("Thank you for using our bank.")