import Monster
import random as r

class Battle:
    def __init__(self):
        self.mon = Monster.monsters
        self.damage = 0
        self.health = 0
        self.agility = 0
        self.defense = 0

    def spawn(self):
        self.c = r.choice(self.mon)
        if r.random() < self.c.chance:
            return self.c
        else:
            return 1

    def create_monster(self, all_heroes):
        avg = 0
        if len(all_heroes) == 1:
            avg = all_heroes[0].lvl
        elif len(all_heroes) == 2:
            avg = (all_heroes[0].lvl + all_heroes[1].lvl) / 2
        elif len(all_heroes) == 3:
            avg = (all_heroes[0].lvl + all_heroes[1].lvl + all_heroes[2].lvl) / 3

        self.damage = self.c.damage
        self.health = self.c.health
        self.agility = self.c.agility
        self.defense = self.c.defense

        for i in range(round(avg)-1):
            self.damage += 20
            self.health += 50
            self.agility += .05

    def update_stats(self, item, action):
        if action == 1:
            if item.effect == 1:
                self.damage -= 10
            elif item.effect == 2:
                self.defense -= 10
            elif item.effect == 3:
                self.agility -= .10
            self.health -= item.dmg
        elif action == 2:
            if item.effect == 1:
                self.damage += 10
            elif item.effect == 2:
                self.defense += 10
            elif item.effect == 3:
                self.agility += .10
        print("Monster Health:", self.health)
        print("Monster Damage:", self.damage)
        print("Monster Defense:", self.defense)

    def print_stats(self):  # Just printing all the stats
        print("Name:       ", self.c.name)
        print("Health:     ", self.health)
        print("Damage:     ", self.damage)
        print("Agility:    ", round(self.agility, 2))
        print("Defense:    ", self.defense, "\n")

