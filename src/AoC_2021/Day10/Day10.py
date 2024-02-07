from aocd.transforms import lines

from src.aoc_frame import run_part

syntax_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_points = {'(': 1, '[': 2, '{': 3, '<': 4}
open_c = '[{(<'
close_c = {'{': '}', '[': ']', '<': '>', '(': ')'}


def part_a(input_data: str) -> str:
    instructions = lines(input_data)
    score = 0

    for line in instructions:

        stack = []
        for c in line:
            if c in open_c:
                stack.append(c)
            else:
                opening = stack.pop()
                if close_c[opening] != c:
                    score += syntax_points[c]
                    break

    return str(score)


def part_b(input_data: str) -> str:
    instructions = lines(input_data)
    scores = []
    
    for line in instructions:
    
        stack = []
        for c in line:
            if c in open_c:
                stack.append(c)
            else:
                opening = stack.pop()
                if close_c[opening] != c:
                    break
        else:
            line_score = 0
            for remaining in stack[::-1]:
                line_score *= 5
                line_score += autocomplete_points[remaining]
            scores.append(line_score)

    scores.sort()
    return str(scores[int(len(scores) // 2)])


run_part(part_a, 'a', 2021, 10)
run_part(part_b, 'b', 2021, 10)

