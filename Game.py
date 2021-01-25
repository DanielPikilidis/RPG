import Player as pl
import Grid as gd
import Items as it
import Market as mk
import Battle as bt
import random
import os

"""
Tune the player, monster and item stats so it's actually playable.
"""


def tutorial():
    print("----How to play:----\n")
    print("-\"H\" Is your current location on the map.")
    print("-\"M\" Are the markets, you can go there to buy or sell items.")
    print("-\"X\" Are the unavailable locations, you can't go there.")
    print("-Every time you move into another area there's a chance a monster will spawn.")
    print("-You can choose to fight the monsters or run away.")
    print("-If you chose more than 1 hero, you can switch between them by typing \"S\"")
    print("-During a battle, when it's your turn to attack, you can type \"cast\" to cast a spell,"
          "\"potion\" to \ndrink a potion and \"attack\" to attack with your equipped weapon(s)."
          "\nYou can also \"switch\" to switch heroes or \"stats\" to show your stats.")
    print("-If you kill the monster you will gain exp and coins.")
    print("-If you gain enough exp, you will level up, "
          "when you level up better items will be available \nin the market.")
    print("-To move you will need to enter \"U\" for up, \"D\" for Down, \"R\" for Right and \"L\" for left.")
    print("-You can open your inventory with \"I\".")
    print("-While in your inventory, you can choose to move items to your hotbar.")
    print("-The hotbar shows you the items you are using.")
    print("-You can always check your stats by typing \"T\".")
    print("-See what's in your hotbar with \"H\".")
    print("-Show the map with \"M\".")
    print("-To exit the game type \"quit\".")
    print("-To show the tutorial again at any time type \"tutorial\".")
    print("-Clear screen with \"clear\".")
    print("-Have fun!\n")


def clear_screen():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('CLS')


def check_input(required_input_list):
    """
    Instead of using a while loop every time I want to check the user's input, I just
    give this function the input I want and it returned the correct value.
    """
    x = input()
    while x.upper() not in required_input_list:
        x = input("Invalid input. Try again: ")
    return x.upper()


def switch_hero(cur, her, hero_lst=None):
    # Checking how many heroes the player has
    if hero_lst is not None:
        if len(hero_lst) == 1:
            cur = hero_lst[0]
            print("Using", cur.name)
        elif len(hero_lst) == 2:
            print("Switch to hero 1 or 2? Type 1 or 2:")
            x = check_input(["1", "2"])
            cur = hero_lst[int(x)-1]
        elif len(hero_lst) == 3:
            print("Switch to hero 1, 2 or 3? Type 1, 2 or 3:")
            x = check_input(["1", "2", "3"])
            cur = hero_lst[int(x)-1]
        return cur

    if her == 1:
        print("You only have 1 hero.")
    elif her == 2:
        print("Switch to hero 1 or 2? Type 1 or 2:")
        x = check_input(["1", "2"])
        x = int(x)
        # Checking if the the requested hero is already equipped and changing him if not
        if x == cur.id == 1:
            print("You are already using", hero1.name)
        elif x == cur.id == 2:
            print("Your are already using", hero2.name)
        elif x == 1:
            cur = hero1
            print("Switched to", hero1.name)
        elif x == 2:
            cur = hero2
            print("Switched to", hero2.name)
    elif her == 3:
        print("Switch to hero 1, 2 or 3? Type 1, 2 or 3:")
        x = check_input(["1", "2", "3"])
        x = int(x)
        # Checking if the the requested hero is already equipped and changing him if not
        if x == cur.id == 1:
            print("You are already using", hero1.name)
        elif x == cur.id == 2:
            print("Your are already using", hero2.name)
        elif x == cur.id == 3:
            print("You are already using", hero3.name)
        elif x == 1:
            cur = hero1
            print("Switched to", hero1.name)
        elif x == 2:
            cur = hero2
            print("Switched to", hero2.name)
        elif x == 3:
            cur = hero3
            print("Switched to", hero3.name)

    return cur  # Current hero in use (his id)


def choose_item():
    print("What do you want to buy? Enter number or \"cancel\" to cancel: ")
    if item_to_buy == "W":
        x = check_input([str(i) for i in range(1, 13)] + ["CANCEL"])
    elif item_to_buy == "A":
        x = check_input([str(i) for i in range(1, 10)] + ["CANCEL"])
    elif item_to_buy == "P" or item_to_buy == "S":
        x = check_input([str(i) for i in range(1, 4)] + ["CANCEL"])
    return x


def equip_item(cur):
    cur.open()
    equipping = True
    while equipping:
        print("Enter a number to move or exit inventory(\"exit\"): ")
        item_to_equip = check_input([str(i) for i in range(1, 11)] + ["EXIT"])
        if item_to_equip.upper() == "EXIT":
            equipping = False
            continue
        c = current_hero.equip(item_to_equip)
        while c == 0 or c == 1:
            if c == 0:
                print("The weapon you want to use requires 2 hands.")
                print("Both of your hands are holding different weapons.")
                print("Your inventory is full so the second item you are holding can't go in your inventory.")
            elif c == 1:
                print("Item is not Weapon or Armor, you don't have to equip it to use it in battle.")
            print("Choose another item to move or exit(\"exit\"): ")
            item_to_equip = check_input([str(i) for i in range(1, 11)] + ["EXIT"])
            if item_to_equip.upper() == "EXIT":
                equipping = False
                break
            while int(item_to_equip) - 1 > len(current_hero.main):
                item_to_equip = str(input("Input should be valid number or \"exit\": "))
                item_to_equip = check_input([str(i) for i in range(1, 11)] + ["EXIT"])
                if item_to_equip.upper() == "EXIT":
                    equipping = False
                    break
            c = cur.equip(item_to_equip)
            cur.update_stats()


def unequip_item(cur):
    cur.open_hotbar()
    moving = True
    while moving:
        print("Enter a number to move or exit hotbar(\"exit\"): ")
        move = check_input([str(i) for i in range(1, 4)] + ["EXIT"])
        if move.upper() == "EXIT":
            moving = False
            continue
        c = current_hero.unequip(move)
        if c == 1:
            print("There's no available space in inventory, go to the market and sell something.")
        else:
            cur.update_stats()


print("Welcome to this game")
# Making sure the player gives a valid number
print("How many heroes do you want? Min:1, Max:3: ")
heroes = check_input(["1", "2", "3"])

heroes = int(heroes)
names = []
types = []
# Getting the names and types for every hero, checking for valid inputs
for i in range(heroes):
    n = str(input("{}) Hero Name(Name should be at least 3 characters and no over 10): ".format(i+1)))
    while len(n) > 10:
        n = str(input("Name can't be over 10 characters: "))
    while len(n) < 3:
        n = str(input("Name can't be less than 3 characters: "))
    print("Hero Type(W=Warrior, S=Sorcerer, P=Paladin): ")
    t = check_input(["W", "S", "P"])
    t = t.upper()
    names.append(n)
    types.append(t)

print("")

# Creating all of the heroes, giving them starting items and stats and printing their stats
all_heroes = []
if heroes == 1:
    hero1 = pl.Hero(types[0], names[0], 1)
    hero1.starterItems()
    hero1.stats()
    hero1.print_hero()
    all_heroes = [hero1]
elif heroes == 2:
    hero1 = pl.Hero(types[0], names[0], 1)
    hero2 = pl.Hero(types[1], names[1], 2)
    hero1.starterItems()
    hero1.stats()
    hero2.starterItems()
    hero2.stats()
    hero1.print_hero()
    hero2.print_hero()
    all_heroes = [hero1, hero2]
elif heroes == 3:
    hero1 = pl.Hero(types[0], names[0], 1)
    hero2 = pl.Hero(types[1], names[1], 2)
    hero3 = pl.Hero(types[2], names[2], 3)
    hero1.starterItems()
    hero1.stats()
    hero2.starterItems()
    hero2.stats()
    hero3.starterItems()
    hero3.stats()
    hero1.print_hero()
    hero2.print_hero()
    hero3.print_hero()
    all_heroes = [hero1, hero2, hero3]

battle = bt.Battle()
grid = gd.Board()   # Initializing the Board class
grid.createGrid()   # Using it to create a grid
tutorial()
market = mk.Shop()  # Initializing the Market class
playing = True
choice = str(input("\nGood! What do you want to do next: "))

current_hero = hero1    # Default hero starting is hero1

while playing:
    current_hero.update_stats()
    choice = choice.upper()
    if choice == "S":
        current_hero = switch_hero(current_hero, heroes)
    elif choice == "M":
        grid.printGrid()
    elif choice in ["U", "D", "R", "L"]:
        direction = choice
        r = grid.move(direction)
        # If there's a market, function will return 1, if there's nothing, return 2
        if r == 1:
            print("Do you want to enter the market? Yes/No: ")
            a = check_input(["YES", "NO"])
            if a.upper() == "YES":
                in_market = True
                while in_market:
                    print("Do you want to Buy or Sell? Enter \"B\" or \"S\": ")
                    sell_or_buy = check_input(["B", "S"])
                    if sell_or_buy.upper() == "S":
                        current_hero.open()
                        item_to_sell = str(input("Enter the number of the item you are willing to sell or cancel: "))
                        if item_to_sell.upper() == "CANCEL":
                            print("Do you want to leave the market? Yes/No: ")
                            leave = check_input(["YES", "NO"])
                            if leave.upper() == "YES":
                                in_market = False
                                break
                            else:
                                continue
                        while int(item_to_sell)-1 > len(current_hero.main) and item_to_sell.upper() != "CANCEL":
                            item_to_sell = str(input("You don't have that many items in your inventory. Enter valid "
                                          "number or cancel: "))
                            if item_to_sell.upper() == "CANCEL":
                                print("Do you want to leave the market? Yes/No: ")
                                leave = check_input(["YES", "NO"])
                                if leave.upper() == "YES":
                                    in_market = False
                                    break
                        else:
                            market.sell(item_to_sell, current_hero)
                            print("Leave market? Yes/No: ")
                            leave = check_input(["YES", "NO"])
                            if leave.upper() == "YES":
                                in_market = False
                                break

                    elif sell_or_buy.upper() == "B":
                        if len(current_hero.main) >= 10 and None not in current_hero.main:
                            print("Your inventory is full, you can't buy any more items. Go back or leave.")
                            print("Go back something or leave: Back/Leave: ")
                            ls = check_input(["BACK", "LEAVE"])
                            if ls.upper() == "BACK":
                                continue
                            else:
                                in_market = False
                                break
                        print("What are you looking to buy? W=Weapons, A=Armor, P=Potions, S=Spells: ")
                        item_to_buy = check_input(["W", "A", "P", "S"])
                        if item_to_buy == "W":
                            market.weapons()    # Prints all weapons
                        elif item_to_buy == "A":
                            market.armors()
                        elif item_to_buy == "P":
                            market.potions()
                        elif item_to_buy == "S":
                            market.spells()     # Returns all the spells in a list
                            how_many = 0
                            owned = []
                            for i in it.spells:     # Checks is the hero owns any of the spells
                                if i in current_hero.main:
                                    how_many += 1
                                    owned.append(i)
                            # If the hero owns any, it will say it
                            if how_many == 3:
                                print("Your hero already knows all of these spells")
                            elif how_many == 2:
                                print("Your hero already knows", owned[0].name, owned[1].name)
                            elif how_many == 1:
                                print("Your hero already knows", owned[0].name)

                        buy = choose_item()
                        if buy.upper() == "CANCEL":
                            print("Do you want to leave the market? Yes/No: ")
                            leave = check_input(["YES", "NO"])
                            if leave.upper() == "YES":
                                in_market = False
                                break
                            else:
                                continue
                        else:
                            c = market.buy(item_to_buy, buy, current_hero)
                            if c == 2:
                                while c == 2 and buy.upper() != "CANCEL":
                                    print("You don't have enough money to buy this item.")
                                    buy = choose_item()
                                    c = market.buy(item_to_buy, buy, current_hero)

                            if c == 1:
                                while c == 1 and buy.upper() != "CANCEL":
                                    print("Your level is not high enough for this item.")
                                    buy = choose_item()
                                    c = market.buy(item_to_buy, buy, current_hero)
                        print("Do you want to leave the market? Yes/No: ")
                        leave = check_input(["YES", "NO"])
                        if leave.upper() == "YES":
                            in_market = False
                            break
        elif r == 2:
            clear_screen()
            grid.printGrid()
            bt = battle.spawn()
            bat = False
            if bt != 1:  # If a monster has appeared
                print("A", bt.name, "appeared!")
                print("Do you want to fight it? Type Yes/No: ")
                ch = check_input(["YES", "NO"])
                if ch.upper() == "YES":
                    battling = True
                else:
                    choice = str(input("What do you want to do next: "))
                    continue

                av_heroes = all_heroes  # Available heroes in battle
                battle.create_monster(all_heroes)
                battle.print_stats()
                rounds = 0
                spell_effect_counter = 0    # Potions and spells last for 3 rounds
                pot_effect_counter = 0
                while battling:
                    if pot_effect_counter >= 4:     # If the effect has been going for 3 rounds, it will go off
                        current_hero.update_stats(sel_pot, 2)
                        pot_effect_counter = 0
                    if spell_effect_counter >= 4:
                        current_hero.update_stats(sel_spell, 2)
                        spell_effect_counter = 0
                    if spell_effect_counter != 0:   # If the effect is active, add 1 more round to it
                        spell_effect_counter += 1
                    if pot_effect_counter != 0:
                        pot_effect_counter += 1
                    print("Your move: ")
                    m = check_input(["CAST", "POTION", "ATTACK", "S", "T", "I"])
                    if m == "S":
                        current_hero = switch_hero(current_hero, len(av_heroes)-1, av_heroes)
                        rounds -= 1
                        if spell_effect_counter > 0:
                            spell_effect_counter -= 2
                        continue
                    elif m == "T":
                        current_hero.print_hero()
                        rounds -= 1
                        if pot_effect_counter > 0:
                            pot_effect_counter -= 2
                        continue
                    elif m == "I":
                        equip_item(current_hero)
                    elif m == "CAST":
                        # Finding all the available spells in the hero's inventory.
                        # Printing them to the player known what he can use
                        # And using the selected one
                        if 0 < spell_effect_counter < 4:
                            print("You still have an spell effect, wait for that to finish to use another one.")
                            spell_effect_counter -= 2
                            continue
                        spell_effect_counter = 0
                        has_spell = False
                        av_spells = []
                        for i in current_hero.main:
                            if i in it.spells:
                                has_spell = True
                                av_spells.append(i)
                        if not has_spell:
                            print("You don't know any spells.")
                            continue
                        else:
                            if current_hero.magic < 24:
                                print("You don't have enough magic power to use this spell.")
                                continue
                            print("Available Spells:")
                            for i in range(len(av_spells)):
                                print(i+1, av_spells[i].name)
                            while True:
                                try:
                                    s = int(input("Which spell do you want to use?(Number): "))
                                    break
                                except ValueError:
                                    print("You have to enter a number!")

                            sel_spell = av_spells[s-1]
                            battle.update_stats(sel_spell, 1)
                            current_hero.magic -= 24
                            spell_effect_counter += 1
                    elif m == "POTION":
                        # Finding all the available potions in the hero's inventory
                        # Printing them so the player knows what he can use
                        # And using the selected one
                        if 0 < pot_effect_counter < 3:
                            print("You still have an potion effect, wait for that to finish to use another one.")
                            pot_effect_counter -= 2
                            continue
                        pot_effect_counter = 0
                        has_potion = False
                        av_pots = []
                        av_pots_ind = []
                        for i in range(len(current_hero.main)):
                            if current_hero.main[i] in it.potion:
                                has_potion = True
                                av_pots.append(current_hero.main[i])
                                av_pots_ind.append(i)
                        if not has_potion:
                            print("You don't have any potions")
                            continue
                        else:
                            print("Available Potions:")
                            for n in range(len(av_pots)):
                                print(n+1, av_pots[n].name)
                            while True:
                                try:
                                    p = int(input("Which potions do you want to use?(Number): "))
                                    break
                                except ValueError:
                                    print("You have to enter a number!")
                            sel_pot = av_pots[p-1]
                            current_hero.update_stats(sel_pot, 1)
                            current_hero.remove(av_pots_ind[p-1])
                            pot_effect_counter += 1
                        continue
                    elif m == "ATTACK":
                        h = random.random()
                        if h < battle.agility:
                            print("The monster avoided your attack!")
                            final_damage_player = 0
                            
                        else:
                            # The final damage of the hit can be +- 30% from the base damage.
                            damage = current_hero.strength
                            a = random.choice([1, 2])
                            if a == 1:
                                alt_damage = damage + (random.random()-.7) * damage
                            else:
                                alt_damage = damage - (random.random() - .7) * damage
                            final_damage_player = round(alt_damage) - battle.defense
                            battle.health -= final_damage_player
                            if battle.health <= 0:
                                print("You killed the monster!")
                                coins = random.choice(range(50, 100))
                                exp = random.choice(range(300, 400))
                                for i in all_heroes:
                                    i.coins += coins
                                    i.experience(exp)
                                    if i.magic == 0:
                                        i.magic += 50
                                    else:
                                        i.magic += (100-i.magic)
                                print("You received {} coins and {} experience.".format(coins, exp))
                                battling = False
                                break
                            print("You did {} damage to the monster({})".format(final_damage_player, battle.health))

                    print("\nMonster's turn to attack.")
                    h = random.random()
                    if h < current_hero.agility:
                        print("You avoided the monster's attack!")
                        continue
                    # Monster's damage can be +- 20% of its base damage
                    damage = battle.damage
                    a = random.choice([1, 2])
                    if a == 1:
                        alt_damage = damage + (random.random()-.8) * damage
                    else:
                        alt_damage = damage + (random.random()-.8) * damage
                    final_damage = round(alt_damage) - current_hero.defense
                    current_hero.health -= abs(final_damage)
                    if current_hero.health <= 0:
                        print("The monster killed you...")
                        # Checking how many heroes there are
                        # If there's more than 1 hero, and there's at least 1 of them alive, it will switch to it
                        # Or if there are 2 heroes alive, it will ask which one to use
                        if heroes == 1:
                            print("You lost the battle and half of your coins.")
                            current_hero.coins /= 2
                            battling = False
                            break
                        else:
                            for i in range(len(av_heroes)):
                                if av_heroes[i] == current_hero:
                                    ind = i
                            av_heroes.pop(ind)
                            if len(av_heroes) == 0:
                                print("All you heroes have died and lost half of their coins.")
                                for i in all_heroes:
                                    i.coins /= 2
                                battling = False
                                break
                            else:
                                print("You have to choose another hero.")
                                print("Remaining heroes:")
                                for i in av_heroes:
                                    print(i.name)
                                current_hero = switch_hero(current_hero, heroes, av_heroes)
                                continue
                    print("The monster did {} damage to you({})".format(abs(round(final_damage)), current_hero.health))
                    rounds += 1
                    battle.health += int(final_damage_player / 2)    # Monster regen every round
                    for i in av_heroes:     # Hero regen every round
                        if i.health + 10 >= 100:
                            i.health = 100
                        else:
                            i.health += 10
                        if i.magic + 10 >= 50:
                            i.magic = 50
                        else:
                            i.magic += 10
                for i in av_heroes:
                    if i.health < 50:
                        i.health += 50
                    else:
                        i.health = 100

                    if i.magic < 25:
                        i.magic += 25
                    else:
                        i.magic = 50

    elif choice == "QUIT":
        playing = False
        break
    elif choice == "CLEAR":
        clear_screen()
    elif choice == "T":
        current_hero.print_hero()
    elif choice == "I":
        equip_item(current_hero)
    elif choice == "TUTORIAL":
        tutorial()
    elif choice == "H":
        unequip_item(current_hero)

    choice = str(input("What do you want to do next: "))
