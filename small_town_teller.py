

class Person:
    
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name 
        self.last_name = last_name

    def __str__(self):
        return "Customer Name: {self.first_name} {self.last_name}, id: {self.id}"


class Account:
    
    def __init__(self, number, acct_type, owner, balance):
        self.number = number
        self.acct_type = acct_type
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account Number: {self.number}, Account Type: {self.acct_type}, Available Balance: {self.balance}"

class Bank:
    
    def __init__(self):
        self.customer_info = Dict[int, Person] 
        self.account_info = Dict[int, Account] 

    def add_customer(self, customer):
        self.customer_info[customer] = customer
        
        


     