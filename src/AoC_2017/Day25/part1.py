from typing import List


class State:

    def __init__(self, write_val: List[int], move_dirs: List[int], new_states: List[int]):
        self.new_states = new_states
        self.move_dirs = move_dirs
        self.write_val = write_val


class Tape:

    def __init__(self):
        # 0 == left, 1 == right
        self.neighbors: List[Tape] = [None, None]
        self.value = 0

    def new_neighbor(self, dir):
        neighbor = Tape()
        self.neighbors[dir] = neighbor
        neighbor.neighbors[dir ^ 1] = self

    def get_neighbor(self, dir):
        if self.neighbors[dir] is None:
            self.new_neighbor(dir)
        return self.neighbors[dir]


# Test States
# states = [State([1, 0], [1, 0], [1, 1]),
#           State([1, 1], [0, 1], [0, 0])]
#
# steps = 6

# Real States
states = [
    State([1, 0], [1, 0], [1, 3]),
    State([1, 0], [1, 1], [2, 5]),
    State([1, 1], [0, 0], [2, 0]),
    State([0, 1], [0, 1], [4, 0]),
    State([1, 0], [0, 1], [0, 1]),
    State([0, 0], [1, 1], [2, 4])
]

steps = 12317297

state = states[0]
count = 0

tape = Tape()

for i in range(steps):
    val = tape.value
    tape.value = state.write_val[val]
    count += (tape.value - val)

    tape = tape.get_neighbor(state.move_dirs[val])
    state = states[state.new_states[val]]

print(count)
