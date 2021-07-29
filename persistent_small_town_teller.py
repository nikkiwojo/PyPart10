import pickle
from small_town_teller import Person, Account

class Bank:

    def __init__(self):
        self.customers = dict()
        self.accounts = dict()

    def add_customer(self, customer):
        customer = Person()
        self.customers[customer.id] = customer

    def add_account(self, account):
        account = Account()
        self.accounts[account.number] = account

    def remove_account(self, account_id):
        self.accounts[account.number].remove()

    def deposit(self, account_id, amount):
        account = self.accounts[account_id]
        account.balance += amount

    def withdrawal(self, account_id, amount):
        account = self.accounts[account_id]
        account.balance -= amount  

    def balance(self, account_id):
        balance = self.accounts.get(account_id).balance
        return balance

    def save_data(self):
        files.save("customers.pickle", self.customers)
        files.save('accounts.pickle', self.accounts)

    def load_data(self):
        self.customers = files.load('customers.pickle')
        self.accounts = files.load('accounts.pickle')

class files:

    def __init__(self):
        pass
    
    def save(file_path, info):
        with open(file_path, 'w') as handler:
            pickle.dump(info, handler)

    def load(file_path):
        with open(file_path, 'r') as handler:
            file = pickle.load(handler)
        return file