import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transaction_list = []
        self.transaction_list.append((Account._current_time(), self.__balance))
        print("Account created for", self.name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))
        else:
            print("It's not possible to deposit a negative amount. [EXCEPTION]")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount needs to be greater than zero and no more than account balance. [EXCEPTION]")

    def show_balance(self):
        print(f"Account balance for {self.name} with balance {self.__balance}.")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount >= 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == '__main__':
    Saito = Account("Saito", 0)
    Saito.show_balance()
    Saito.deposit(1000)
    Saito.show_balance()
    Saito.withdraw(500)
    Saito.show_balance()
    Saito.show_transactions()
    Saito.show_balance()
    print(Saito.__dict__)
