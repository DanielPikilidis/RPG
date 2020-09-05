import Items as it


class Hero:
    def __init__(self, typ, name, id):
        self.main = [None]*10
        self.hotbar = [None]*3  # Weapon1, Weapon2, Armor
        self.lvl = 1
        self.coins = 30
        self.exp = 0
        self.typ = typ  # Hero Type
        self.health = 100
        self.magic = 50
        self.name = name
        self.id = id
        self.strength = 0
        self.dexterity = 0
        self.agility = 0
        self.defense = 0

    def starterItems(self):     # Starter items different for every hero type
        if self.typ == "W":
            self.main[0] = it.starter_weapon2    # Gold Sword
            self.main[1] = it.starter_armor1     # Gold Armor
        elif self.typ == "S":
            self.main[0] = it.starter_weapon1    # Bronze Sword
            self.main[1] = it.spell2     # FireSpell
        elif self.typ == "P":
            self.main[0] = it.starter_weapon1    # Bronze Sword
            self.main[1] = it.potion2    # Swiftness Potion
            self.main[2] = it.potion2    # same...

    def stats(self):    # Every hero type has different stats
        if self.typ == "W":
            self.base_strength = 20
            self.base_dexterity = 10
            self.base_agility = .15
            self.base_defense = 10
        elif self.typ == "S":
            self.base_strength = 10
            self.base_dexterity = 20
            self.base_agility = .15
            self.base_defense = 5
        elif self.typ == "P":
            self.base_strength = 20
            self.base_dexterity = 20
            self.base_agility = .10
            self.base_defense = 10

        self.strength = self.base_strength
        self.dexterity = self.base_dexterity
        self.agility = self.base_agility
        self.defense = self.base_defense

    def update_stats(self, item=None, action=0):
        self.strength = self.base_strength
        self.dexterity = self.base_dexterity
        self.agility = self.base_agility
        self.defense = self.base_defense

        if self.hotbar[0] is not None:
            item1 = self.hotbar[0]
            if item1.two_hands:
                self.strength += (self.base_strength/100) * item1.dmg
            else:
                if self.hotbar[1] is not None:
                    item2 = self.hotbar[1]
                    self.strength += (self.base_strength/100) * item1.dmg + (self.base_strength/100) * item2.dmg
                else:
                    self.strength += (self.base_strength/100) * item1.dmg

        if self.hotbar[2] is not None:
            item3 = self.hotbar[2]
            self.defense += (self.base_defense/100) * item3.defense

        if item is not None:
            if action == 1:     # Using the spell
                if item in it.potion:
                    if item.effect == 1:
                        self.strength += 8
                    elif item.effect == 2:
                        self.agility += .15
                    elif item.effect == 3:
                        self.defense += 8
            elif action == 2:       # The effects of the potion stop because the 3 rounds have passed
                if item in it.potion:
                    if item.effect == 1:
                        self.strength -= 8
                    elif item.effect == 2:
                        self.agility -= .15
                    elif item.effect == 3:
                        self.defense -= 8

        self.strength = round(self.strength)
        self.defense = round(self.defense)

    def open_hotbar(self):
        print("Viewing hotbar...")
        for i in range(len(self.hotbar)):
            if self.hotbar[i] is None:
                print(i+1, "Empty Slot")
            else:
                print(i+1, self.hotbar[i].name)

    def open(self):
        print("Opening inventory...")
        for i in range(len(self.main)):
            if self.main[i] is None:
                print(i+1, "Empty Slot")
            else:
                print(i+1, self.main[i].name)

    def add(self, item):
        for i in range(len(self.main)):
            if self.main[i] is None:
                self.main[i] = item
                break
        print("Added:", item.name, "to inventory.")

    def remove(self, ind):
        self.main[ind] = None

    def equip(self, ind):
        ind = int(ind) - 1
        item = self.main[ind]
        if item in it.weapon or item == it.starter_weapon1 or item == it.starter_weapon2:
            if item.two_hands:  # If the item requires 2 hands
                if self.hotbar[0] is None and self.hotbar[1] is None:    # Only if both weapon slots are empty
                    print("Equipped", item.name, "on hotbar slot 1 and 2")
                    self.main[ind], self.hotbar[0] = self.hotbar[0], self.main[ind]
                else:
                    if None in self.main:
                        ind2 = self.main.index(None)
                        self.main[ind], self.hotbar[0] = self.hotbar[0], self.main[ind]
                        self.main[ind2], self.hotbar[1] = self.hotbar[1], self.main[ind2]
                        print("Equipped", item.name, "on hotbar slot 1")
            else:
                if self.hotbar[0] is None:
                    self.hotbar[0], self.main[ind] = self.main[ind], None
                    print("Equipped", item.name, "on hotbar slot 1")
                elif self.hotbar[0].two_hands:
                    return 0
                elif self.hotbar[1] is None:
                    self.hotbar[1], self.main[ind] = self.main[ind], None
                    print("Equipped", item.name, "on hotbar slot 2")
                else:
                    choice = str(input("Switch to hotbar slot 1 or 2?"))
                    while choice not in ["1", "2"]:
                        choice = str(input("Input should be 1 or 2"))
                    if int(choice) == 1:
                        self.main[ind], self.hotbar[0] = self.hotbar[0], self.main[ind]
                    else:
                        self.main[ind], self.hotbar[1] = self.hotbar[1], self.main[ind]
        elif item in it.armor or item == it.starter_armor1:
            self.main[ind], self.hotbar[2] = self.hotbar[2], self.main[ind]
            print("Equipped", item.name, "on hotbar slot 3")
        elif item not in it.armor and item not in it.weapon:
            return 1    # Item not Weapon or Armor, can't be equipped

    def unequip(self, ind):
        ind = int(ind) - 1
        item = self.hotbar[ind]
        if None in self.main:
            i = self.main.index(None)
            self.hotbar[ind], self.main[i] = self.main[i], self.hotbar[ind]
            print("Unequipped", item.name)
        else:
            return 0    # No available space in inventory

    def money(self, amount):
        if amount < 0:
            self.coins += amount
            print("Removed", amount, "coins from player.")
        elif amount > 0:
            self.coins += amount
            print("Added", amount, "coins to player.")

    def level(self):    # If the hero gets enough experience(function below) he levels up
        self.lvl += 1
        print("You leveled up!()".format(self.lvl))

    def experience(self, amount):
        self.exp += amount
        if self.lvl == 1 and self.exp >= 500:
            self.level()
        elif self.lvl == 2 and self.exp >= 1000:
            self.level()
        elif self.lvl == 3 and self.exp >= 2000:
            self.level()
        elif self.lvl == 4 and self.exp >= 4000:
            self.level()

    def print_hero(self):    # Just printing all the stats
        if self.typ == "W":
            t = "Warrior"
        elif self.typ == "S":
            t = "Sorcerer"
        else:
            t = "Paladin"
        print("Name:       ", self.name)
        print("Type:       ", t)
        print("Level:      ", self.lvl)
        print("Experience: ", self.exp)
        print("Coins:      ", self.coins)
        print("Health:     ", self.health)
        print("Magic Power:", self.magic)
        print("Strength:   ", self.strength)
        print("Dexterity:  ", self.dexterity)
        print("Agility:    ", self.agility)
        print("Defense:    ", self.defense, "\n")
