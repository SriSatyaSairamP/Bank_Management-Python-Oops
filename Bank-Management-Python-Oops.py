from abc import ABC,abstractmethod

class Bank:
    bank_name = "Python Bank"
    
    branches = {
        "CodeHaven": {
            "branch_code": "1001",
            "ifsc_code": "PYBA001001"
        },
        "ByteVille": {
            "branch_code": "1002",
            "ifsc_code": "PYBA001002"
        },
        "LogicPoint": {
            "branch_code": "1003",
            "ifsc_code": "PYBA001003"
        },
        "AlgoCity": {
            "branch_code": "1004",
            "ifsc_code": "PYBA001004"
        },
        "SyntaxPark": {
            "branch_code": "1005",
            "ifsc_code": "PYBA001005"
        },
        "DataNest": {
            "branch_code": "1006",
            "ifsc_code": "PYBA001006"
        },
        "LoopTown": {
            "branch_code": "1007",
            "ifsc_code": "PYBA001007"
        },
        "PixelBay": {
            "branch_code": "1008",
            "ifsc_code": "PYBA001008"
        },
        "CloudBridge": {
            "branch_code": "1009",
            "ifsc_code": "PYBA001009"
        },
        "StackSquare": {
            "branch_code": "1010",
            "ifsc_code": "PYBA001010"
        }
    }
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
    next_account_number= 10000000001

    @classmethod
    def _generate_account_number(cls):
        account_number=cls.next_account_number
        if len(str(account_number))!=11:
            raise ValueError("Account number must contain exactly 11 digits.")
        cls.next_account_number +=1
        return account_number


    def __init__(self,name,branch_name,balance):

        if branch_name not in Bank.branches:
            raise ValueError("Invalid Branch name.")
        self._validate_amount(balance)

        self.account_number = Account._generate_account_number()
        self.name=name
        self.branch_name=branch_name
        self.branch_code=Bank.branches[branch_name]["branch_code"]
        self.ifsc_code =Bank.branches[branch_name]["ifsc_code"]

        self.__balance = float(balance)
        self.transactions =[]

        self.transactions.append(f"Initial Deposit: +₹{balance:.2f}")

        Bank.register_account(self)

        print(
            f"\n{self.__class__.__name__} created successfully"
            f"\nBank Name       : {Bank.bank_name}"
            f"\nBranch Name     : {self.branch_name}"
            f"\nIFSC Code       : {self.ifsc_code}"
            f"\nAccount Number  : {self.account_number}"
            f"\nAccount Holder  : {self.name}"
            f"\nInitial Deposit : ₹{self.get_balance():.2f}"

        )


    def _validate_amount(self,amount):
        if isinstance(amount,bool) or not isinstance(amount,(int,float)):
            raise TypeError("Amount should be NUMERIC!")
        elif amount<=0:
            raise ValueError("Amount should be greater than zero.")

    def get_balance(self):
        return self.__balance

    def _set_balance(self,amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance=float(amount)

    def deposit(self,amount):
        self._validate_amount(amount)
        self._set_balance(self.get_balance()+amount)
        self.transactions.append(f"+₹{amount:.2f} Deposited")
        print(
            f"\n₹{amount:.2f} deposited successfully into {self.name}'s account "
            f"(Account No: {self.account_number}). "
            f"Current Balance: ₹{self.get_balance():.2f}."
        )

    @abstractmethod
    def withdraw(self,amount):
        pass

    def _deduct(self,amount):
        self._set_balance(self.get_balance()-amount)

    def display(self):
        print(f"\nBank Name      : {Bank.bank_name}")
        print(f"Branch Name    : {self.branch_name}")
        print(f"IFSC Code      : {self.ifsc_code}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Account Type   : {self.__class__.__name__}")
        print(f"Balance        : ₹{self.get_balance():.2f}")


    def show_transactions(self):
        print(f"\nTransaction History")
        print(f"Bank Name      : {Bank.bank_name}")
        print(f"Branch Name    : {self.branch_name}")
        print(f"IFSC Code      : {self.ifsc_code}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Account Type   : {self.__class__.__name__}")
        print(f"Transactions:")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(Account):

    def withdraw(self,amount):
        self._validate_amount(amount)
        if amount > 40000:
            print("\nDaily Limit Exceeded.")
        elif amount > self.get_balance():
            print("\nInsufficient Balance.")
        else:
            self._deduct(amount)
            self.transactions.append(f"-₹{amount:.2f} Withdrawn")
            print(
                f"\nWithdrawal of ₹{amount:.2f} from {self.name}'s account "
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
            self.transactions.append(f"-₹{amount:.2f} Withdrawn")
            print(
                f"\nWithdrawal of ₹{amount:.2f} from {self.name}'s account "
                f"(Account No: {self.account_number}) was successful. "
                f"Current Balance: ₹{self.get_balance():.2f}."
            )

Bank.display_all_accounts()
Bank.display_total_balance()

acc1=SavingsAccount("Atharv","CodeHaven",5000)
acc2=CurrentAccount("Nancy","LogicPoint",9000)
acc1.withdraw(600)
acc2.deposit(5000)
acc2.withdraw(16000)
acc1.display()
acc2.show_transactions()
Bank.display_all_accounts()
Bank.display_total_balance()








