from abc import ABC,abstractmethod

class Account(ABC):

    def __init__(self,name,balance):
        self.name=name
        self._validate_amount(balance)
        self.__balance=float(balance)

    def _validate_amount(self,amount):
        if not isinstance(amount,(int,float)):
            raise TypeError("Amount should be NUMERIC!")
        elif amount<0:
            raise ValueError("Amount Should not be Negative.")

    def get_balance(self):
        return self.__balance

    def set_balance(self,amount):
        self._validate_amount(amount)
        self.__balance=float(amount)

    def deposit(self,amount):
        self._validate_amount(amount)
        new_balance=self.get_balance()+amount
        self.set_balance(new_balance)
        print(f"₹{amount} deposited successfully")

    @abstractmethod
    def withdraw(self,amount):
        pass

    def display(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Balance: {self.get_balance()}")

    def _deduct(self,amount):
        new_balance=self.get_balance()-amount
        self.set_balance(new_balance)

class SavingsAccount(Account):

    def withdraw(self,amount):
        self._validate_amount(amount)
        if amount>self.get_balance():
            print("Insufficient Balance")
        elif amount>40000:
            print("Daily Limit Exceeded")
        else:
            self._deduct(amount)
            print(f"₹{amount} withdrawn successfully")


class CurrentAccount(Account):

    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self.get_balance():
            print("Insufficient Balance")
        else:
            self._deduct(amount)
            print(f"₹{amount} withdrawn successfully")

class Bank:

    def __init__(self,total):
        self.total=total

    def __add__(self,other):
        return Bank(self.total+other.total)

    def display_total(self):
        print(f"\nTotal Bank Balance: ₹{self.total}")

acc1=SavingsAccount("Sai",10000)
acc2=CurrentAccount("Ishaan",20000)

acc1.display()
print(acc2.get_balance())
acc1.deposit(5000)
acc2.withdraw(2000)
acc2.display()

bank1=Bank(acc1.get_balance())
bank2=Bank(acc2.get_balance())
bank1.display_total()

total=bank1+bank2
total.display_total()
