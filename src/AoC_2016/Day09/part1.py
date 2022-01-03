import re

pattern = re.compile("\\(([0-9]+)x([0-9]+)\\)")


def decompress(compressed: str) -> int:
    match = pattern.search(compressed)
    while match is not None:
        char_count = int(match.group(1))
        repeats = int(match.group(2))
        start_pos = match.start()
        end_pos = match.end()

        compressed = compressed[:start_pos] + (compressed[end_pos:end_pos + char_count] * repeats) + \
                     compressed[end_pos + char_count:]
        match = pattern.search(compressed, start_pos + (char_count * repeats))

    return len(compressed)


assert (decompress("ADVENT") == 6)
assert (decompress("A(1x5)BC") == 7)
assert (decompress("(3x3)XYZ") == 9)
assert (decompress("A(2x2)BCD(2x2)EFG") == 11)
assert (decompress("(6x1)(1x3)A") == 6)
assert (decompress("X(8x2)(3x3)ABCY") == 18)

print(decompress(open("input.txt").read().splitlines()[0]))


def decompress_v2(compressed: str) -> int:
    match = pattern.search(compressed)
    length = 0
    while match is not None:
        char_count = int(match.group(1))
        repeats = int(match.group(2))
        start_pos = match.start()
        end_pos = match.end()

        length += start_pos + (decompress_v2(compressed[end_pos:end_pos + char_count]) * repeats)
        compressed = compressed[end_pos + char_count:]
        match = pattern.search(compressed)

    return len(compressed) + length


assert (decompress_v2("(3x3)XYZ") == 9)
assert (decompress_v2("X(8x2)(3x3)ABCY") == 20)
assert (decompress_v2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920)
assert (decompress_v2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445)

print(decompress_v2(open("input.txt").read().splitlines()[0]))