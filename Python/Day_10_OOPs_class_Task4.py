#bank account system
'''implement a class BankAccount that supports the following operations
deposit monet
withdraw money(if sufficient balance avalibla)
check balance'''

class BankAccount:
    def __init__(self,account_holder, balance = 0):
        #account_holder for individual name accessing
        #defalut balance is take zero
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited. current balance:${self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Inufficient funds")
        else:
            self.balance-=amount
            print(f"{amount} withdrawn. current balance:${self.balance}")
    def check_balance(self):
        print(f"Account holder: {self.account_holder}, Balance:${self.balance}")
obj=BankAccount("Bhivi",100)
'''obj.deposit(50)
obj.withdraw(30)
obj.check_balance()'''
#for repeatation
choice =1 #1 is True
while choice!=0:#it itterate upto choice=0
    print("0.Exit")#condition if false Exit
    print("1. deposit")
    print("2. withdraw")
    print("3. check_balance")
    choice=int(input("Enter Choice: "))
    if choice == 1:
        obj.deposit(50)
    elif choice == 2:
        obj.withdraw(30)
    elif choice == 3:
        obj.check_balance()
    elif choice == 0:
        print("Exiting!!!")
    else:
        print("invalid choice...")
