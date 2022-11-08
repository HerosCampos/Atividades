class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount


monster = Monster(100, 75)
#print(monster.health, monster.energy)
#monster.energy += 25
#print(monster.health, monster.energy)

monster.update_energy(20)
print(monster.energy)

        