
from typing import Self


class FinancialCalculatorMixin:
    def __init__(self, accounts: list["BankAccount"] = None):
        self.accounts: list[BankAccount] = []
        if accounts:
            self.accounts: list[BankAccount] = accounts

    @property
    def money(self) -> int:
        # my_money = 0
        # for account in self.accounts:
        #     my_money += account.balance

        summs = [account.balance for account in self.accounts]
        print(summs)
        return sum(summs)

    def __eq__(self, other: Self):
        return self.money == other.money

    def __ge__(self, other: Self):
        return self.money >= self.money

    def __gt__(self, other: Self):
        return self.money > other.money


class Person(FinancialCalculatorMixin):
    def __init__(self, name: str):
        super().__init__()
        self.name = name.strip().title()
        print('created ', self)

    def __str__(self):
        return f"Person {self.name}"


class BankAccount:
    def __init__(self, owner: Person, bank: "Bank"):
        self.balance = 0
        self.owner = owner
        self.bank = bank
        print(self)

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount

    def transfer_money(self, other: Self, amount: int):
        self.balance -= amount
        other.balance += amount
        print(f'Money transferred {amount} ({self} -> {other})')


    def __str__(self):
        return f"Account was opened in {self.bank} for {self.owner.name}"


class Bank(FinancialCalculatorMixin):
    def __init__(self, title: str):
        super().__init__()
        self.title = f'LTD {title.strip().upper()}'
        print(self)

    def open_account(self, client: Person) -> BankAccount:
        bank_account = BankAccount(owner=client, bank=self)
        self.accounts.append(bank_account)
        client.accounts.append(bank_account)
        return bank_account

    def __str__(self):
        return f"{self.title}"