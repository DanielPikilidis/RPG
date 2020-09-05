class Weapon:
    def __init__(self, name, price, lvl, dmg, two_hands):
        self.name = name
        self.price = price
        self.lvl = lvl
        self.dmg = dmg
        self.two_hands = two_hands

    def view(self, ind):
        n = 1 - ind//9                  # All this to make the
        n2 = 16 - len(self.name)        # weapon list as pretty
        n3 = 1 - self.price//100        # and easy to read as possible
        if not self.two_hands:
            print(ind+1, " "*n + self.name, " "*n2, self.price, " "+" "*n3, self.lvl, "   ", self.dmg)
        else:
            print(ind+1, " "*n + self.name, " "*n2, self.price, " "+" "*n3, self.lvl, "   ", self.dmg, "   ",
                  "This weapon requires 2 hands to use.")


class Armor:
    def __init__(self, name, price, lvl, defense):
        self.name = name
        self.price = price
        self.lvl = lvl
        self.defense = defense

    def view(self, ind):
        n = 17 - len(self.name)
        n2 = 2 - self.price // 100
        print(ind+1, self.name, " "*n, self.price, " "*n2, self.lvl, "   ", self.defense)


class Potion:
    def __init__(self, name, price, effect, lvl):
        self.name = name
        self.price = price
        self.effect = effect
        self.lvl = lvl

    def view(self, ind):
        n = 17 - len(self.name)
        if self.effect == 1:
            effect = "Hero gains 8 Strength for a few rounds"
        elif self.effect == 2:
            effect = "Hero gains 8 Agility for a few rounds"
        elif self.effect == 3:
            effect = "Hero gains 8 Defense for a few rounds"

        print(ind+1, self.name, " "*n, self.price, "  ", effect)


class Spell:
    def __init__(self, name, price, dmg, effect, lvl):
        self.name = name
        self.price = price
        self.dmg = dmg
        self.effect = effect
        self.lvl = lvl

    def view(self, ind):
        n = 17 - len(self.name)
        if self.effect == 1:
            effect = "Enemy loses 10 strength for a few rounds"
        elif self.effect == 2:
            effect = "Enemy loses 10 defense for a few rounds"
        elif self.effect == 3:
            effect = "Enemy loses 10 agility for a few rounds"
        print(ind+1, self.name, " " * n, self.price, "  ", self.dmg, "  ", effect)
        return self.name


weapon = []
armor = []
potion = []
spells = []

# Creating instances of all in-game items
# Weapon          name, price, level, damage, 2 hands
weapon1 = Weapon("Arkhalis", 30, 1, 20, False)
weapon.append(weapon1)
weapon2 = Weapon("Blood Butcherer", 35, 1, 22, False)
weapon.append(weapon2)
weapon3 = Weapon("Falcon Blade", 45, 2, 30, False)
weapon.append(weapon3)
weapon4 = Weapon("Ice Sickle", 60, 2, 55, True)
weapon.append(weapon4)
weapon5 = Weapon("Cutlass", 55, 3, 49, False)
weapon.append(weapon5)
weapon6 = Weapon("Death Sickle", 80, 3, 80, True)
weapon.append(weapon6)
weapon7 = Weapon("Excalibur", 100, 4, 68, False)
weapon.append(weapon7)
weapon8 = Weapon("Keybrand", 115, 4, 72, False)
weapon.append(weapon8)
weapon9 = Weapon("Terra Blade", 140, 5, 85, False)
weapon.append(weapon9)
weapon10 = Weapon("Tizona", 160, 5, 90, False)
weapon.append(weapon10)
weapon11 = Weapon("Star Wrath", 200, 5, 95, True)
weapon.append(weapon11)
weapon12 = Weapon("Flying Dragon", 230, 5, 100, True)
weapon.append(weapon12)
starter_weapon1 = Weapon("Bronze Sword", 10, 1, 4, False)
starter_weapon2 = Weapon("Gold Sword", 15, 1, 8, False)

# Armor         name, price, level, protection
armor1 = Armor("Spectre Armor", 25, 1, 30)
armor.append(armor1)
armor2 = Armor("Beetle Armor", 35, 1, 33)
armor.append(armor2)
armor3 = Armor("Titan Armor", 48, 2, 41)
armor.append(armor3)
armor4 = Armor("Dragon Armor", 65, 3, 50)
armor.append(armor4)
armor5 = Armor("Shinobi Armor", 72, 3, 55)
armor.append(armor5)
armor6 = Armor("Valhalla Armor", 88, 4, 64)
armor.append(armor6)
armor7 = Armor("Vortex Armor", 98, 4, 72)
armor.append(armor7)
armor8 = Armor("Nebula Armor", 120, 5, 88)
armor.append(armor8)
armor9 = Armor("Stardust Armor", 140, 5, 100)
armor.append(armor9)
starter_armor1 = Armor("Gold Armor", 10, 1, 12)

# Potion          name, price, effect
potion1 = Potion("Rage Potion", 30, 1, 0)
potion.append(potion1)
potion2 = Potion("Swiftness Potion", 30, 2, 0)
potion.append(potion2)
potion3 = Potion("Tank Potion", 30, 3, 0)
potion.append(potion3)

# Spell         name, price, damage, effect
spell1 = Spell("IceSpell", 100, 15, 1, 0)
spells.append(spell1)
spell2 = Spell("FireSpell", 100, 15, 2, 0)
spells.append(spell2)
spell3 = Spell("LightningSpell", 100, 15, 3, 0)
spells.append(spell3)
