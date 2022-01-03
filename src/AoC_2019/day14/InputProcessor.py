import copy
from collections import deque

from src.day14.ChemStore import ChemStore
from src.day14.Reaction import Reaction


def process_file(filename):
    print("processing file " + filename)
    file = open(filename)
    input_lines = file.read().splitlines()

    reactions = {}

    build_reactions(input_lines, reactions)
    return reactions


def part1(reactions):
    chem_store = ChemStore()
    reaction_records = deque()
    target_fuel = 1
    return create_fuel(chem_store, reaction_records, reactions, target_fuel)


def create_fuel(chem_store, reaction_records, reactions, target_fuel):
    chem_store.needed["FUEL"] = target_fuel
    while len(chem_store.needed) > 0:
        key, value = list(chem_store.needed.items())[0]
        reaction_records.appendleft(chem_store.react(reactions[key], value))
    # print(chem_store.ore_count)
    return chem_store.ore_count


def part2(reactions):
    chem_store = ChemStore()
    reaction_records = deque()
    current_fuel = 0
    MAX_ORE = 1_000_000_000_000
    power = 30
    while power >= 0:
        new_chem_store = copy.deepcopy(chem_store)
        new_ore = create_fuel(new_chem_store, reaction_records, reactions, 2**power)
        if new_ore < MAX_ORE:
            chem_store = new_chem_store
            current_fuel += 2**power
        power -= 1

    return current_fuel


def build_reactions(input_lines, reactions):
    for i in input_lines:
        reaction = Reaction(i)
        reactions[reaction.output_type] = reaction
