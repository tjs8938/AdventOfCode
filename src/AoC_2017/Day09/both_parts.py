import re


def count_groups(string: str) -> int:
    string = re.sub('!.', '', string)
    string = re.sub('<[^>]*>', '', string)

    score = 0
    group_count = 0
    for c in string:
        if c == '{':
            group_count += 1
        elif c == '}':
            score += group_count
            group_count -= 1

    return score


def count_garbage(string: str) -> int:
    string = re.sub('!.', '', string)
    no_garbage = re.sub('<[^>]*>', '<>', string)

    return len(string) - len(no_garbage)


input_string = open("input.txt").read().splitlines()[0]
print(count_groups(input_string))
print(count_garbage(input_string))