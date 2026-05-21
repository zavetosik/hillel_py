class Person:
    def __init__(self, name: str, address: str = "") -> None:
        self.first_name = name.strip().title()
        self.money = 0
        self.tin = id(self)
        self.address = address

    def __str__(self) -> str:
        return f'<{self.first_name}: {self.tin}. Money: {self.money}grn>'

    def deposit_money(self, amount: float):
        self.money += amount

    @property
    def is_reach(self) -> bool:
        return self.money > 10_000

person_1 = Person(name='   alex')
print(id(person_1))

print(person_1.__dict__)
print(person_1)

person_1_money_usd = person_1.money / 44.30
print(person_1_money_usd)
person_1.money += 10000
print(person_1)

person_1.deposit_money(111)
print(person_1)

is_reach = person_1.is_reach
print(is_reach)
person_2 = Person(name='Angelina', address='Odesa')
print(person_1.__dict__)
print(person_2.__dict__)
