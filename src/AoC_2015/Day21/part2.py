import itertools
from math import ceil

weapons = [("Dagger", 8, 4, 0),
           ("Shortsword", 10, 5, 0),
           ("Warhammer", 25, 6, 0),
           ("Longsword", 40, 7, 0),
           ("Greataxe", 74, 8, 0)]

armor = [("Leather", 13, 0, 1),
         ("Chainmail", 31, 0, 2),
         ("Splintmail", 53, 0, 3),
         ("Bandedmail", 75, 0, 4),
         ("Platemail", 102, 0, 5)]

rings = [("Damage +1", 25, 1, 0),
         ("Damage +2", 50, 2, 0),
         ("Damage +3", 100, 3, 0),
         ("Defense +1", 20, 0, 1),
         ("Defense +2", 40, 0, 2),
         ("Defense +3", 80, 0, 3)]


configs = []

for w in weapons:
    configs.append((w[1], w[2], w[3]))


for c in configs.copy():
    for a in armor:
        configs.append((a[1] + c[0], a[2] + c[1], a[3] + c[2]))

for c in configs.copy():
    for r in rings:
        configs.append((r[1] + c[0], r[2] + c[1], r[3] + c[2]))

    for r1, r2 in itertools.combinations(rings, 2):
        configs.append((r1[1] + r2[1] + c[0], r1[2] + r2[2] + c[1], r1[3] + r2[3] + c[2]))

configs.sort(key=lambda x: x[0])
configs.reverse()

boss_attack = 8
boss_armor = 2
boss_hp = 109

for config in configs:
    my_attack = config[1]
    my_armor = config[2]
    my_hp = 100

    if ceil(boss_hp/max(my_attack - boss_armor, 1)) > ceil(my_hp/max(boss_attack - my_armor, 1)):
        print(ceil(boss_hp/max(my_attack - boss_armor, 1)))
        print(ceil(my_hp/max(boss_attack - my_armor, 1)))
        print(config)
        break
