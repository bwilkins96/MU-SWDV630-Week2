# SWDV 630 - Object-Oriented Software Architecture
# Driver that instantiates CheckingAccount instances and performs debits/credits

from checking_account import CheckingAccount

def print_acc_info(acc_obj):
    """Formats and prints info about passed-in CheckingAccount object"""
    header = f'{acc_obj.name()}: {acc_obj.account_number()}'    
    print(header)
    print('-' * len(header))
    print(f'Current Balance: $ {acc_obj.balance():.2f} \n')

def main():
    account_1 = CheckingAccount('John Doe', '1234 Sunny Way', 1000050)
    account_2 = CheckingAccount('Jane Flower', '5678 Moon Drive', 100060)

    account_1.credit(500)
    account_2.credit(15000)

    print()
    print_acc_info(account_1)
    print_acc_info(account_2)

    account_1.debit(50)
    account_1.debit(65.45)
    account_2.debit(5745)

    print_acc_info(account_1)
    print_acc_info(account_2)

if __name__ == '__main__': main()