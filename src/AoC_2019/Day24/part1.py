def build_bitmask(*args) -> int:
    value = 0
    for a in args:
        value += pow(2, a)
    return value


TOP_LEFT = build_bitmask(1, 5)
TOP = build_bitmask(0, 2, 6)
TOP_RIGHT = build_bitmask(3, 9)
LEFT = build_bitmask(0, 6, 10)
INSIDE = build_bitmask(1, 5, 7, 11)
RIGHT = build_bitmask(4, 8, 14)
BOTTOM_LEFT = build_bitmask(15, 21)
BOTTOM = build_bitmask(20, 16, 22)
BOTTOM_RIGHT = build_bitmask(23, 19)
BITMASKS = [TOP_LEFT, TOP, TOP << 1, TOP << 2, TOP_RIGHT,
            LEFT, INSIDE, INSIDE << 1, INSIDE << 2, RIGHT,
            LEFT << 5, INSIDE << 5, INSIDE << 6, INSIDE << 7, RIGHT << 5,
            LEFT << 10, INSIDE << 10, INSIDE << 11, INSIDE << 12, RIGHT << 10,
            BOTTOM_LEFT, BOTTOM, BOTTOM << 1, BOTTOM << 2, BOTTOM_RIGHT
            ]


def count_enabled_bits(val: int) -> int:
    count = 0
    while val > 0:
        val = val & (val - 1)
        count += 1
    return count


def get_next_bio_value(biodiversity_rating):
    next_bio_rating = biodiversity_rating
    index_mask = 1
    for index in range(0, 25):
        surrounding_spaces = biodiversity_rating & BITMASKS[index]
        if biodiversity_rating & index_mask > 0:
            # This space has a bug
            if count_enabled_bits(surrounding_spaces) != 1:
                # the number of neighbors is not exactly 1, so kill the bug
                next_bio_rating ^= index_mask
        else:
            # this space is empty
            if count_enabled_bits(surrounding_spaces) in [1, 2]:
                # infest this space
                next_bio_rating ^= index_mask
        index_mask <<= 1

    return next_bio_rating


def part1(filename: str) -> int:
    input_chars = "".join(open(filename).read().splitlines())
    pow = 1
    biodiversity_rating = 0
    for c in input_chars:
        if c == '#':
            biodiversity_rating += pow
        pow <<= 1

    prev_bio_values = set()

    while biodiversity_rating not in prev_bio_values:
        prev_bio_values.add(biodiversity_rating)
        biodiversity_rating = get_next_bio_value(biodiversity_rating)

    return biodiversity_rating


print(part1("test1.txt"))
print(part1("input.txt"))
