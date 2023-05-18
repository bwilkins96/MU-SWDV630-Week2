# SWDV 630 - Object-Oriented Software Architecture
# Checking account class

class CheckingAccount:
    def __init__(self, name, address, acc_num):
        self._name = name.capitalize()
        self._address = address
        self._account_number = acc_num
        self._balance = 0.0

    def name(self):
        return self._name
    
    def address(self):
        return self._address
    
    def account_number(self):
        return self._account_number
    
    def balance(self):
        return self._balance
    
    def set_name(self, name):
        self._name = name.capitalize()

    def set_address(self, address):
        self._address = address

    def credit(self, amt):
        self._balance += amt

    def debit(self, amt):
        self._balance -= amt