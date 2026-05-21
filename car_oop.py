class Car:
    def __init__(self, model: str, age: int, owner: str = "", fuel: float = 0) -> None:
        self.model = model.strip().title()
        self.age = age
        self.owner = owner
        self.fuel = fuel
        self.car_id = id(self)

    def __str__(self) -> str:
        return f"<{self.model}, {self.age} років, власник: {self.owner or 'немає'}, бензин: {self.fuel} л>"

    def refuel(self, amount: float):
        self.fuel += amount

    @property
    def condition(self) -> str:
        if self.age <= 3:
            return "Нове авто"
        elif 4 <= self.age <= 10:
            return "Середній стан"
        else:
            return "Старе авто"

    @property
    def fuel_status(self) -> str:
        if self.fuel < 5:
            return "Потрібно заправитись"
        elif 5 <= self.fuel < 20:
            return "Достатньо бензину"
        else:
            return "Можна їхати далеко"


car_1 = Car(model="Toyota Corolla", age=2, owner="Alex")
car_2 = Car(model="Ford Focus", age=7)

print(id(car_1))
print(id(car_2))

print(car_1.__dict__)
print(car_2.__dict__)

print(car_1)
print(car_2)

car_1.fuel += 4
print(car_1)

car_2.refuel(15)
print(car_2)

print(car_1.condition)
print(car_2.condition)

if car_1.fuel > car_2.fuel:
    print(f"Більше бензину у {car_1.model}")
else:
    print(f"Більше бензину у {car_2.model}")

print(car_1.fuel_status)
print(car_2.fuel_status)