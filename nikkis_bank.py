from small_town_teller import Person, Account, Bank
from persisten_small_town_teller import Person, Account, Bank

nikkis_bank = Bank()
bob = Person(1,'Bob', 'Smith')
print(nikkis_bank.add_customer(bob))

nikkis_bank = Bank()
nikkis_bank.load_data()