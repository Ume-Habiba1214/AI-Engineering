class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def display(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance : {self.balance}")

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            return self.balance
        else:
            return None







bankholder1=BankAccount("Ali",100)
bankholder1.deposit(500)
bankholder1.deposit(200)
bankholder1.deposit(500)
bankholder1.display()
current_balance = bankholder1.get_balance()
print(current_balance)
remaining_balance=bankholder1.withdraw(500)
if remaining_balance is None:
    print("Insufficient balance")
else:
    print(f"Remaining Balance : {remaining_balance}")