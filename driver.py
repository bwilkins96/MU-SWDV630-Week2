# SWDV 630 - Object-Oriented Software Architecture
# Driver that instantiates CheckingAccount instances and performs debits/credits

from checking_account import CheckingAccount

def main():
    account_1 = CheckingAccount('John Doe', '1234 Sunny Way', 1000050)
    account_2 = CheckingAccount('Jane Flower', '5678 Moon Drive', 100060)

    account_1.credit(500)
    account_2.credit(15000)

    print(account_1.balance())
    print(account_2.balance())

    account_1.debit(50)
    account_2.debit(5745)

    print(account_1.balance())
    print(account_2.balance())

if __name__ == '__main__': main()