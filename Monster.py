from RPG import Grid as gd

class Monster:
    def __init__(self, name, damage, health, agility, defense, chance):
        self.name = name
        self.damage = damage
        self.health = health
        self.agility = agility
        self.defense = defense
        self.chance = chance


#                   Name    Damage, health, Agility, defense, chance
monster1 = Monster("Dragon", 19, 600, .12, 5, .06)
monster2 = Monster("Exoskeleton", 15, 700, .15, 10, .11)
monster3 = Monster("Spirit", 13, 700, .18, 5, .08)
monsters = [monster1, monster2, monster3]
