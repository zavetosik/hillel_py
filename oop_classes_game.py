from abc import ABC, abstractmethod
from typing import Self


class Character(ABC):
    def __init__(self, ammo: int, hp: int):
        self.__ammo = ammo
        self.__hp = hp

    @property
    def is_alive(self) -> bool:
        return self.__hp > 0

    @property
    def ammo(self) -> int:
        return self.__ammo

    @property
    def hp(self) -> int:
        return self.__hp

    @abstractmethod
    def __str__(self) -> str:
        return ''

    def attack(self, other: Self):
        if not self.is_alive:
            print('I am dead now ((((')
            return

        if not self.__ammo > 0:
            print('No weapon')
            return

        self.__ammo -= 1
        other.__hp -= 30


class Tank(Character):
    def __init__(self, model: str, ammo: int = 20):
        super().__init__(ammo, hp=100)
        self.model = model

    def __str__(self) -> str:
        return f"Tank {self.model} with ammo={self.ammo}"


class Soldier(Character):
    def __init__(self, name: str, ammo: int = 2):
        super().__init__(ammo, hp=25)
        self.name = name

    def __str__(self) -> str:
        return f"Soldier {self.name} with hp={self.hp} and ammo={self.ammo}"


class Worm(Character):
    def __str__(self) -> str:
        return f"Worm with hp={self.hp} and ammo={self.ammo}"


tank1 = Tank('Abrams')
soldier1 = Soldier('Alex')
worm = Worm(ammo=1, hp=1)

print(tank1.__dict__)
print(worm.is_alive, 444)
tank1.attack(worm)
print(tank1.__dict__)
print(worm.is_alive, 444)
worm.attack(tank1)


tank2 = Tank('Abrams')
tank4 = Tank('Abrams', 10)
tank3 = Tank('Tiger', ammo=35)

# print(tank3.__dict__)
# print(tank3.is_alive)
#
# tank3.__hp = 0
# print(tank3.is_alive)
# print(tank3.__dict__)
# print(tank3.is_alive)
#
# print(tank3.ammo)
#
# print(soldier1.is_alive)