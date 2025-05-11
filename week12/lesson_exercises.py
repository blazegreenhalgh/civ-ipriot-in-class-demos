from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        super().__init__
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def area(self):
        return self.length * self.width


circle = Circle(10)
print(circle.area())

rectangle = Rectangle(10, 5)
print(rectangle.area())



class BankAccount():
    def __init__(self, _account_number, _balance):
        self._account_number = _account_number
        self._balance = _balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def view_balance(self):
        return self._balance

my_bank = BankAccount(12345, 100)

print(my_bank.view_balance())
my_bank.withdraw(50)
print(my_bank.view_balance())
my_bank.deposit(10)
print(my_bank.view_balance())

class Payment(ABC):
    @abstractmethod
    def authorize_transaction(self, bank_account, amount):
        ...

class DebitCardPayment(Payment): 
    def authorize_transaction(self, bank_account, amount):
        if bank_account.view_balance() - amount >= 0:
            bank_account.withdraw(amount)
            print(f"Payment processed! Remaining balance: {bank_account.view_balance()}")
        else:
            print("Payment failed - insufficient funds")

class CreditCardPayment(Payment): 
    def authorize_transaction(self, bank_account, amount):
        bank_account.withdraw(amount)
        print(f"Payment processed! Remaining balance: {bank_account.view_balance()}")

CreditCardPayment().authorize_transaction(my_bank, 100)
DebitCardPayment().authorize_transaction(my_bank, 100)

