from typing import Set, List

from src.AoC_2016.Day11.State import State

THULIUM = 1
PLUTONIUM = 2
STRONTIUM = 4
PROMETHIUM = 8
RUTHENIUM = 16
ELERIUM = 32
DILITHIUM = 64

start_state: State = State()
start_state.elevator = 0
start_state.generators = [[THULIUM, PLUTONIUM, STRONTIUM, ELERIUM, DILITHIUM],
                          [],
                          [PROMETHIUM, RUTHENIUM],
                          []]
start_state.microchips = [[THULIUM, ELERIUM, DILITHIUM],
                          [PLUTONIUM, STRONTIUM],
                          [PROMETHIUM, RUTHENIUM],
                          []]

end_state: State = State()
end_state.elevator = 3
end_state.generators = [[], [], [], [THULIUM, PLUTONIUM, STRONTIUM, PROMETHIUM, RUTHENIUM, ELERIUM, DILITHIUM]]
end_state.microchips = [[], [], [], [THULIUM, PLUTONIUM, STRONTIUM, PROMETHIUM, RUTHENIUM, ELERIUM, DILITHIUM]]

generated_states: Set[State] = set()
generated_states.add(start_state)

states_to_process: List[State] = [start_state]

while len(states_to_process) > 0:
    state = states_to_process.pop(0)
    next_states: List[State] = State.state_generator(state)
    for s in next_states:
        if s not in generated_states:
            if s == end_state:
                print(s.steps)
                exit(0)
            else:
                generated_states.add(s)
                states_to_process.append(s)
