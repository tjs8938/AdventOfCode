from src.Utility.MatrixPrint import pair_to_key, position_to_key, dict_to_matrix, print_matrix

# input_file = open("test1.txt")
input_file = open("input.txt")

input_lines = input_file.read().splitlines()

EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'

all_seats = {}
prev_state = 0
new_state = 1


class Seat:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbor_count = [0, 0]
        self.state = [EMPTY, EMPTY]

    def __repr__(self):
        return self.state[prev_state]

    def update(self):
        count = 0
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if i != self.x or j != self.y:
                    key = position_to_key(i, j)
                    if key in all_seats and all_seats[key].state[prev_state] == OCCUPIED:
                        count += 1

        self.neighbor_count[new_state] = count
        if count == 0:
            self.state[new_state] = OCCUPIED
        elif count >= 4:
            self.state[new_state] = EMPTY
        else:
            self.state[new_state] = self.state[prev_state]

        return self.state[new_state]


for y in range(0, len(input_lines)):
    for x in range(0, len(input_lines[y])):
        if input_lines[y][x] == EMPTY:
            all_seats[position_to_key(x, y)] = Seat(x, y)

print(all_seats)
total_occupied = 0
new_occupied = 0
while True:
    print_matrix(dict_to_matrix(all_seats, xform=lambda s: s.state[prev_state]))
    for seat in all_seats.values():
        new_occupied += 1 if seat.update() == OCCUPIED else 0

    if new_occupied == total_occupied:
        break
    else:
        total_occupied = new_occupied
        new_occupied = 0
        new_state = new_state ^ 1
        prev_state = prev_state ^ 1

print(total_occupied)