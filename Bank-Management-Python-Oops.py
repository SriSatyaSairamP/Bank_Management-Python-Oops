from abc import ABC,abstractmethod

class Bank:
    bank_name = "Python Bank"
    accounts=[]
    savings_accounts=[]
    current_accounts=[]

    @classmethod
    def register_account(cls,account):
        cls.accounts.append(account)

        if isinstance(account,SavingsAccount):
            cls.savings_accounts.append(account)
        elif isinstance(account,CurrentAccount):
            cls.current_accounts.append(account)

    @classmethod
    def display_all_accounts(cls):
        print(f"\nAll Accounts in {cls.bank_name}")

        if not cls.accounts:
            print("No accounts have been registered yet.")
        else:
            for account in cls.accounts:
                account.display()

    @classmethod
    def display_total_balance(cls):
        total=0
        for account in cls.accounts:
            total+=account.get_balance()
        print(f"\nTotal Bank Balance: ₹{total:.2f}")


class Account(ABC):
    next_account_number= 10001
    
    def __init__(self,name,branch_name,balance):
        self.account_number = Account.next_account_number
        Account.next_account_number +=1
        self.name=name
        self.branch_name=branch_name
        self._validate_amount(balance)
        self.__balance = float(balance)
        self.transactions =[]

        self.transactions.append(f"Initial Deposit: +₹{balance}")

        Bank.register_account(self)

        print(
            f"\n{self.__class__.__name__} created successfully"
            f"\nBank Name       : {Bank.bank_name}"
            f"\nBranch Name     : {self.branch_name}"
            f"\nAccount Number  : {self.account_number}"
            f"\nAccount Holder  : {self.name}"
            f"\nInitial Deposit : ₹{self.get_balance():.2f}"

        )


    def _validate_amount(self,amount):
        if not isinstance(amount,(int,float)):
            raise TypeError("Amount should be NUMERIC!")
        elif amount<=0:
            raise ValueError("Amount should be greater than zero.")

    def get_balance(self):
        return self.__balance

    def set_balance(self,amount):
        self._validate_amount(amount)
        self.__balance=float(amount)

    def deposit(self,amount):
        self._validate_amount(amount)
        self.set_balance(self.get_balance()+amount)
        self.transactions.append(f"+₹{amount} Deposited")
        print(
            f"\n₹{amount} deposited successfully into {self.name}'s account "
            f"(Account No: {self.account_number}). "
            f"Current Balance: ₹{self.get_balance():.2f}."
        )

    @abstractmethod
    def withdraw(self,amount):
        pass

    def _deduct(self,amount):
        self.set_balance(self.get_balance()-amount)

    def display(self):
        print(f"\nBank Name      : {Bank.bank_name}")
        print(f"Branch Name    : {self.branch_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Account Type   : {self.__class__.__name__}")
        print(f"Balance        : ₹{self.get_balance():.2f}")


    def show_transactions(self):
        print(f"\nTransaction History")
        print(f"Bank Name      : {Bank.bank_name}")
        print(f"Branch Name    : {self.branch_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Account Type   : {self.__class__.__name__}")
        print(f"Transactions:")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(Account):

    def withdraw(self,amount):
        self._validate_amount(amount)
        if amount>self.get_balance():
            print(f"\nInsufficient Balance.")
        elif amount>40000:
            print(f"\nDaily Limit Exceeded.")
        else:
            self._deduct(amount)
            self.transactions.append(f"-₹{amount} Withdrawn")
            print(
                f"\nWithdrawal of ₹{amount} from {self.name}'s account "
                f"(Account No: {self.account_number}) was successful. "
                f"Current Balance: ₹{self.get_balance():.2f}."
            )


class CurrentAccount(Account):

    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self.get_balance():
            print("\nInsufficient Balance.")
        else:
            self._deduct(amount)
            self.transactions.append(f"-₹{amount} Withdrawn")
            print(
                f"\nWithdrawal of ₹{amount} from {self.name}'s account "
                f"(Account No: {self.account_number}) was successful. "
                f"Current Balance: ₹{self.get_balance():.2f}."
            )

Bank.display_all_accounts()
Bank.display_total_balance()
acc1=SavingsAccount("Atharv","Mot",5000)
acc2=CurrentAccount("Nancy","Hyt",9000)
acc1.withdraw(600)
acc2.deposit(5000)
acc2.withdraw(16000)
acc1.display()
acc2.show_transactions()
Bank.display_all_accounts()
Bank.display_total_balance()





