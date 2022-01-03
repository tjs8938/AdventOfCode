from __future__ import annotations

import itertools
from copy import deepcopy
from typing import List


class State:

    def __init__(self):
        self.generators: List[List[int]] = [[], [], [], []]
        self.microchips: List[List[int]] = [[], [], [], []]
        self.elevator = 0
        self.steps = 0

    def __hash__(self):
        gen_sums = list(map(lambda floor: sum(floor), self.generators))
        chip_sums = list(map(lambda floor: sum(floor), self.microchips))
        return hash((str(gen_sums), str(chip_sums), self.elevator))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def is_valid(self) -> bool:
        for floor in range(len(self.microchips)):
            for chip in self.microchips[floor]:
                if len(self.generators[floor]) > 0 and chip not in self.generators[floor]:
                    return False
        return True

    @staticmethod
    def clone(state: State, new_floor: int) -> State:
        s = deepcopy(state)
        s.elevator = new_floor
        s.steps += 1
        return s

    @staticmethod
    def move_floors(start_state: State, new_floor: int) -> List[State]:
        floor = start_state.elevator
        new_states = []

        # Create all "Single Generator" moves
        for g in start_state.generators[floor]:
            s = State.clone(start_state, new_floor)
            s.generators[floor].remove(g)
            s.generators[new_floor].append(g)
            State.add_if_valid(new_states, s)

        # Create all " Two Generator" moves
        if len(start_state.generators[floor]) > 1:
            for g1, g2 in itertools.combinations(start_state.generators[floor], 2):
                s = State.clone(start_state, new_floor)

                s.generators[floor].remove(g1)
                s.generators[new_floor].append(g1)
                s.generators[floor].remove(g2)
                s.generators[new_floor].append(g2)

                State.add_if_valid(new_states, s)

        # Create all "Single Microchip" moves
        for c in start_state.microchips[floor]:
            s = State.clone(start_state, new_floor)
            s.microchips[floor].remove(c)
            s.microchips[new_floor].append(c)
            State.add_if_valid(new_states, s)

        # Create all "Two Microchip" moves
        if len(start_state.microchips[floor]) > 1:
            for c1, c2 in itertools.combinations(start_state.microchips[floor], 2):
                s = State.clone(start_state, new_floor)

                s.microchips[floor].remove(c1)
                s.microchips[new_floor].append(c1)
                s.microchips[floor].remove(c2)
                s.microchips[new_floor].append(c2)

                State.add_if_valid(new_states, s)

        # Special handling when the match generator and microchip are on this floor
        for c in start_state.microchips[floor]:
            if c in start_state.generators[floor]:
                s = State.clone(start_state, new_floor)
                s.microchips[floor].remove(c)
                s.microchips[new_floor].append(c)
                s.generators[floor].remove(c)
                s.generators[new_floor].append(c)
                State.add_if_valid(new_states, s)

        return new_states

    @staticmethod
    def add_if_valid(new_states: List[State], s: State):
        if s.is_valid():
            new_states.append(s)

    @staticmethod
    def state_generator(start_state: State) -> List[State]:
        new_states = []
        if start_state.elevator > 0:
            new_states.extend(State.move_floors(start_state, start_state.elevator - 1))

        if start_state.elevator < 3:
            new_states.extend(State.move_floors(start_state, start_state.elevator + 1))

        return new_states
