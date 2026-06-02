from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        print(f"₹{amount} deposited successfully")

    @abstractmethod
    def withdraw(self,amount):
        pass

    def display(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Balance: {self.__balance}")

class SavingsAccount(Account):

    def withdraw(self,amount):
        if amount>self.get_balance():
            print("Insufficient Balance")
        elif amount>40000:
            print("Daily Limit Exceeded!")
        else:
            new_balance=self.get_balance()-amount
            self.set_balance(new_balance)
            print(f"₹{amount} withdrawn successfully")

class CurrentAccount(Account):

    def withdraw(self,amount):
        if amount>self.get_balance():
            print("Insufficient Balance")
        else:
            new_balance=self.get_balance()-amount
            self.set_balance(new_balance)
            print(f"₹{amount} withdrawn successfully")

class Bank:

    def __init__(self,total):
        self.total=total

    def __add__(self,other):
        return Bank(self.total+other.total)

    def show_total(self):
        print(f"\nTotal Bank Balance: {self.total}")

acc1=SavingsAccount("Sai",10000)
acc2=CurrentAccount("Ishaan",20000)

acc1.display()
print(acc2.get_balance())
acc1.deposit(5000)
acc2.withdraw(2000)
acc2.display()

bank1=Bank(acc1.get_balance())
bank2=Bank(acc2.get_balance())
bank1.show_total()

total=bank1+bank2
total.show_total()
