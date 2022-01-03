from __future__ import annotations
import re

# Group 1 -  which group (immune/infection)
# Group 2 -  unit count (int)
# Group 3 -  hit points (int)
# Group 5 -  comma separated list of "weak" effects
# Group 9 -  comma separated list of "immune" effects
# Group 11 - attack points (int)
# Group 12 - attack effect
# Group 13 - initiative (int)
from dataclasses import dataclass
from typing import List, Dict

pattern = re.compile(
    "(immune|infection): ([0-9]*) units each with ([0-9]*) hit points \(?(weak to ([^;)]*))?(; )?(\) )?\(?(immune to ([^;)]*))?(\) )?with an attack that does ([0-9]*) ([^ ]*) damage at initiative ([0-9]*)")


@dataclass
class Squad:
    index: int
    army: str
    units: int
    hit_points: int
    weak_effects: List[str]
    immune_effects: List[str]
    attack_points: int
    attack_effect: str
    initiative: int

    def __hash__(self):
        return hash((self.army, self.index))

    def get_effective_power(self):
        return self.units * self.attack_points

    def damage_against_target(self, target: Squad):
        multiplier = 1
        if self.attack_effect in target.weak_effects:
            multiplier = 2
        elif self.attack_effect in target.immune_effects:
            multiplier = 0
        return self.get_effective_power() * multiplier


def choose_targets(a_squads, d_squads, targets, debug=False):
    for a_squad in a_squads:
        if a_squad.units == 0:
            continue

        current_target = None
        highest_damage = 0
        for d_squad in d_squads:
            if d_squad.units > 0 and d_squad not in targets.values() and d_squad.army != a_squad.army:
                potential_damage = a_squad.damage_against_target(d_squad)
                if debug:
                    print("{} group {} would deal defending group {} {} damage".format(a_squad.army,
                                                                                       a_squad.index,
                                                                                       d_squad.index,
                                                                                       potential_damage))
                if potential_damage > highest_damage:
                    highest_damage = potential_damage
                    current_target = d_squad

        if current_target is not None:
            targets[a_squad] = current_target


def fight(boost=0, debug=False):
    squads: List[Squad] = []
    immune_squads: List[Squad] = []
    infection_squads: List[Squad] = []

    live_immune_squads = 0
    live_infection_squads = 0

    # filename = "test1.txt"
    filename = "input.txt"
    for line in open(filename).read().splitlines():
        m = pattern.match(line)
        new_squad = Squad(0,
                          m.group(1),
                          int(m.group(2)),
                          int(m.group(3)),
                          [] if m.group(5) is None else m.group(5).split(', '),
                          [] if m.group(9) is None else m.group(9).split(', '),
                          int(m.group(11)),
                          m.group(12),
                          int(m.group(13))
                          )
        squads.append(new_squad)
        if new_squad.army == 'immune':
            live_immune_squads += 1
            immune_squads.append(new_squad)
            new_squad.index = live_immune_squads
            new_squad.attack_points += boost
        else:
            live_infection_squads += 1
            infection_squads.append(new_squad)
            new_squad.index = live_infection_squads

    while live_immune_squads > 0 and live_infection_squads > 0:
        if debug:
            print()
            print("Immune System")
            for s in immune_squads:
                if s.units > 0:
                    print("Group ", s.index, " contains ", s.units, " units")

            print("Infection")
            for s in infection_squads:
                if s.units > 0:
                    print("Group ", s.index, " contains ", s.units, " units")

        immune_squads.sort(key=lambda x: (x.get_effective_power(), x.initiative), reverse=True)
        infection_squads.sort(key=lambda x: (x.get_effective_power(), x.initiative), reverse=True)
        targets: Dict[Squad, Squad] = {}

        if debug:
            print()
        choose_targets(infection_squads, immune_squads, targets)
        choose_targets(immune_squads, infection_squads, targets)

        squads.sort(key=lambda x: x.initiative, reverse=True)

        if debug:
            print()
        for attacking_squad in squads:
            if attacking_squad in targets:
                defending_squad = targets[attacking_squad]
                if attacking_squad.units > 0:
                    damage = attacking_squad.damage_against_target(defending_squad)
                    units_killed = min(damage // defending_squad.hit_points, defending_squad.units)
                    if debug:
                        print(attacking_squad.army, "group", attacking_squad.index, "attacks defending group",
                              defending_squad.index, ", killing", units_killed, "units")
                    if units_killed >= defending_squad.units:
                        defending_squad.units = 0
                        if defending_squad.army == 'immune':
                            live_immune_squads -= 1
                        else:
                            live_infection_squads -= 1
                    else:
                        defending_squad.units -= units_killed

    return sum(map(lambda x: x.units, immune_squads)), sum(map(lambda x: x.units, infection_squads))


print("Part 1: ", fight())

print("Part 2")
boost_attempts = [100, 50, 25, 37, 36, 35, 34]
for b in boost_attempts:
    print("boost {}: {}".format(b, fight(b)))

