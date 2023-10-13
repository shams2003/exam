import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(1000, 9999)
        self.transactions = []
        self.loan_taken = 0
        self.transfer_enabled = True

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'Deposit: +{amount}')
            return f'Deposited {amount} into your account.'
        else:
            return 'Invalid deposit amount.'

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Withdraw: -{amount}')
            return f'Withdrawn {amount} from your account.'
        else:
            return 'Withdrawal amount exceeded. Insufficient balance.'

    def check_balance(self):
        return f'Available balance: {self.balance}'

    def transaction_history(self):
        return self.transactions

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken = 1
            self.balance += amount
            self.transactions.append(f'Loan Taken: +{amount}')
            return f'Loan of {amount} credited to your account.'
        else:
            return 'You have already taken the maximum number of loans.'

    def transfer_amount(self, recipient, amount):
        if self.transfer_enabled and recipient:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transactions.append(f'Transfer: -{amount} to {recipient.name}')
                recipient.transactions.append(f'Transfer: +{amount} from {self.name}')
                return f'Transferred {amount} to {recipient.name}.'
            else:
                return 'Insufficient balance for the transfer.'
        else:
            return 'Account does not exist or transfers are disabled.'

    def enable_transfers(self):
        self.transfer_enabled = True

    def disable_transfers(self):
        self.transfer_enabled = False

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                return f'Account {account_number} has been deleted.'
        return 'Account not found.'

    def list_accounts(self):
        account_list = []
        for user in self.users:
            account_list.append((user.name, user.account_number))
        return account_list

    def total_balance(self):
        total = sum(user.balance for user in self.users)
        return f'Total available balance in the bank: {total}'

    def total_loan_amount(self):
        total = sum(user.loan_taken for user in self.users)
        return f'Total loan amount in the bank: {total}'

    def enable_loans(self):
        for user in self.users:
            user.enable_transfers()

    def disable_loans(self):
        for user in self.users:
            user.disable_transfers()


if __name__ == "__main__":
    admin = Admin()

    user1 = admin.create_account("User1", "user1@example.com", "Address1", "Savings")
    user2 = admin.create_account("User2", "user2@example.com", "Address2", "Current")

    user1.deposit(1000)
    user2.deposit(2000)

    print(user1.check_balance())
    print(user2.check_balance())

    user1.withdraw(500)
    user2.withdraw(2500)

    print(user1.check_balance())
    print(user2.check_balance())

    user1.transfer_amount(user2, 300)

    admin.enable_loans()

    print(user1.take_loan(1000))
    print(user1.take_loan(5000))
    print(user2.take_loan(2000))

    print(admin.list_accounts())
    print(admin.total_balance())
    print(admin.total_loan_amount())

    admin.disable_loans()
