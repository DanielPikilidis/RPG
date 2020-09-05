import Player as pl
import Items as it


class Shop:
    def __init__(self):
        self.items = []
        self.weapon = it.weapon
        self.armor = it.armor
        self.potion = it.potion
        self.spell = it.spells

    def weapons(self):
        self.items = it.weapon
        print("  Name               Price Level Damage")
        for i in range(len(it.weapon)):
            it.weapon[i].view(i)


    def armors(self):
        self.items = it.armor
        print("  Name               Price Level Damage")
        for i in range(len(it.armor)):
            it.armor[i].view(i)

    def potions(self):
        self.items = it.potion
        print("  Name               Price Effect")
        for i in range(len(it.potion)):
            it.potion[i].view(i)

    def spells(self):
        self.items = it.spells
        print("  Name               Price Damage Effect")
        for i in range(len(it.spells)):
            it.spells[i].view(i)

    def buy(self, typ, num, current_hero):    # Type, Num, Current Hero
        ind = int(num) - 1
        coins = current_hero.coins
        if typ == "W":
            item = self.weapon[ind]
        elif typ == "A":
            item = self.armor[ind]
        elif typ == "P":
            item = self.potion[ind]
        elif typ == "S":
            item = self.spell[ind]

        if coins >= item.price and current_hero.lvl >= item.lvl:
            current_hero.money(-item.price)
            current_hero.add(item)
            return 0
        elif current_hero.lvl < item.lvl:
            return 1
        elif coins <= item.price:
            return 2

    def sell(self, num, current_hero):
        ind = int(num) - 1
        item = current_hero.main[ind]
        sell_price = int(item.price/2)
        current_hero.remove(ind)
        current_hero.money(sell_price)
