
class Tank:
    def __init__(self, model: str, ammo: int = 20):
        self.model = model
        self._ammo = ammo
        self._hp = 100

    @property
    def is_alive(self) -> bool:
        return self._hp > 0

class Soldier:
    def __init__(self, name: str, ammo: int = 2):
        self.name = name
        self.ammo = ammo
        self.hp = 25

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

tank1 = Tank('Abrams')
soldier1 = Soldier('Alex')


tank2 = Tank('Abrams')
tank4 = Tank('Abrams')
tank3 = Tank('Tiger', ammo=35)

print(tank3.__dict__)
print(tank3.is_alive)

tank3.hp = 0
print(tank3.is_alive)



