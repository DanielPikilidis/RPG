import random

damage = 15
for i in range(10):
    s = random.choice([1, 2])
    if s == 1:
        alt_damage = damage + (random.random()-.7) * damage
    else:
        alt_damage = damage - (random.random()-.7) * damage
    print(round(alt_damage))