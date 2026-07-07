from abc import ABC,abstractmethod

class Account(ABC):
    next_account_number= 10001
    
    def __init__(self,name,balance):
        self.account_number = Account.next_account_number
        Account.next_account_number +=1
        self.name=name
        self._validate_amount(balance)
        self.transactions =[]
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
        self.transactions.append(f"+₹{amount} Deposited")
        print(f"{self.name} (Account No: {self.account_number}) deposited ₹{amount} successfully. Current Balance: ₹{self.get_balance()}")

    @abstractmethod
    def withdraw(self,amount):
        pass

    def display(self):
        print(f"\nAccount NUmber: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.get_balance()}")

    def _deduct(self,amount):
        new_balance=self.get_balance()-amount
        self.set_balance(new_balance)

    def show_transactions(self):
        print(f"\nTransaction History")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        if not self.transactions:
            print("No transactions found")
        else:
            for transaction in self.transactions:
                print(transaction)


class SavingsAccount(Account):

    def withdraw(self,amount):
        self._validate_amount(amount)
        if amount>self.get_balance():
            print("Insufficient Balance")
        elif amount>40000:
            print("Daily Limit Exceeded")
        else:
            self._deduct(amount)
            self.transactions.append(f"-₹{amount} Withdrawn")
            print(f"Withdrawal of ₹{amount} from {self.name}'s account (Account No: {self.account_number}) was successful. Current Balance: ₹{self.get_balance()}")


class CurrentAccount(Account):

    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self.get_balance():
            print("Insufficient Balance")
        else:
            self._deduct(amount)
            self.transactions.append(f"-₹{amount} Withdrawn")
            print(f"Withdrawal of ₹{amount} from {self.name}'s account (Account No: {self.account_number}) was successful. Current Balance: ₹{self.get_balance()}")

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
acc1.withdraw(2000)
acc2.withdraw(2000)
acc2.display()

bank1=Bank(acc1.get_balance())
bank2=Bank(acc2.get_balance())
bank1.display_total()

total=bank1+bank2
total.display_total()

acc1.show_transactions()
