import json
import math

from src.AoC_2019.day14.Reaction import Reaction


class ReactionRecord(object):
    def __init__(self, r):
        self.count = 0
        self.used_from_stores = {}
        self.used_from_input = {}
        self.added_to_stores = {}
        self.produced = {}
        self.reaction = r

    def __repr__(self):
        return str(self.reaction) + " * " + str(self.count) + "\nUsed from stores: " + str(self.used_from_stores) + ", Used from inputs: " + str(self.used_from_input) + ", Added to stores: " + str(self.added_to_stores) + ", Produced: " + str(self.produced)


class ChemStore(object):
    def __init__(self):
        self.ore_count = 0
        self.materials = {}
        self.needed = {}
        self.produced = {}

    def __eq__(self, o: object) -> bool:
        return isinstance(o, ChemStore) and self.materials == o.materials and self.needed == o.needed

    def __hash__(self) -> int:
        return hash((json.dumps(self.materials, sort_keys=True), json.dumps(self.needed, sort_keys=True)))

    def __repr__(self):
        return ("Available Materials: " + str(self.materials) + "\n" +
                "Needed Materials: " + str(self.needed) + "\n" +
                "Produced Materials: " + str(self.produced))

    def react(self, reaction: Reaction, count_needed: int) -> ReactionRecord:
        record = ReactionRecord(reaction)
        t = reaction.output_type

        if self.materials.get(t, 0) > count_needed:
            record.used_from_stores[t] = count_needed
            self.materials[t] -= count_needed
            count_needed = 0
        else:
            record.used_from_stores[t] = self.materials.get(t, 0)
            count_needed -= self.materials.get(t, 0)
            self.materials[t] = 0

        reaction_count = math.ceil(count_needed / reaction.output_count)
        record.count = reaction_count
        record.produced[t] = reaction.output_count * reaction_count

        self.materials[t] = self.materials.get(t, 0) + (record.produced[t] - count_needed)
        record.added_to_stores[t] = record.produced[t] - count_needed
        self.produced[t] = self.produced.get(t, 0) + record.produced[t]
        del self.needed[t]

        for i in reaction.inputs:
            needed = reaction_count * reaction.inputs[i]
            record.used_from_input[i] = needed

            if i == 'ORE':
                self.ore_count += needed
            else:
                if self.materials.get(i, 0) > needed:
                    self.materials[i] = self.materials.get(i, 0) - needed
                else:
                    self.needed[i] = self.needed.get(i, 0) + needed - self.materials.get(i, 0)
                    if self.needed[i] == 0:
                        del self.needed[i]

                    self.materials[i] = 0

        return record
