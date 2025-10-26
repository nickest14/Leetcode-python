# 2043. Simple Bank System

from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance: List[int] = balance
        self.n: int = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            not self.validate(account1)
            or not self.validate(account2)
            or self.balance[account1 - 1] < money
        ):
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.validate(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.validate(account) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True

    def validate(self, account: int) -> bool:
        return 1 <= account <= self.n


obj = Bank([10, 100, 20, 50, 30])
print(obj.withdraw(3, 10))
print(obj.transfer(5, 1, 20))
print(obj.deposit(5, 20))
print(obj.transfer(3, 4, 15))
print(obj.withdraw(10, 50))
