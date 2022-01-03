from collections import defaultdict, deque

from aocd.transforms import lines

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    caves = defaultdict(set)
    for line in lines(input_data):
        data = line.split('-')
        caves[data[0]].add(data[1])
        caves[data[1]].add(data[0])

    complete_paths = set()
    queue = deque()
    queue.append('start')
    while len(queue) > 0:
        path = queue.popleft()
        cave = path.split('-')[-1]
        for n in caves[cave]:
            if n == 'end':
                new_path = path + '-' + n
                complete_paths.add(new_path)
            elif n.islower() and path.find(n) >= 0:
                continue
            else:
                new_path = path + '-' + n
                queue.append(new_path)

    return len(complete_paths)


def part_b(input_data: str) -> str:
    caves = defaultdict(set)
    for line in lines(input_data):
        data = line.split('-')
        caves[data[0]].add(data[1])
        caves[data[1]].add(data[0])

    complete_paths = set()
    queue = deque()
    queue.append(('start', False))
    while len(queue) > 0:
        p = queue.popleft()
        path = p[0]
        double_small = p[1]
        cave = path.split('-')[-1]
        for n in caves[cave]:
            new_double_small = double_small
            if n == 'start':
                continue
            if n == 'end':
                new_path = path + '-' + n
                complete_paths.add(new_path)
                continue
            elif n.islower():
                if path.count(n) == 0 or (path.count(n) == 1 and not double_small):
                    if path.count(n) == 1:
                        new_double_small = True
                else:
                    continue

            new_path = path + '-' + n
            queue.append((new_path, new_double_small))

    return len(complete_paths)


# run_part(part_a, 'a', 2021, 12)
run_part(part_b, 'b', 2021, 12)


