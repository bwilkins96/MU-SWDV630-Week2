# SWDV 630 - Object-Oriented Software Architecture
# Checking account class

class CheckingAccount:
    """Checking Account class designed for Maryville University"""

    def __init__(self, name, address, acc_num):
        """
        Sets up a CheckingAccount instance with a passed-in name, address, and account number.
        Starting balance is set to zero.
        """
        self._name = name.title()
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
        self._name = name.title()

    def set_address(self, address):
        self._address = address

    def credit(self, amt):
        """Adds amt to the account's balance"""
        self._balance += amt

    def debit(self, amt):
        """Subtracts amt from the account's balance"""
        self._balance -= amt

    def __repr__(self):
        return f'(Account {self.account_number()}, {self.name()}: ${self.balance():.2f})'