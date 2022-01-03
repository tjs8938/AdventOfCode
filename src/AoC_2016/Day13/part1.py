from typing import Tuple, List, Set, Dict

fav_number = 1364
TARGET = (31, 39)


def is_open(x: int, y: int) -> bool:
    loc_id = x*x + 3*x + 2*x*y + y + y*y
    loc_id += fav_number
    open_space = True
    while loc_id > 0:
        open_space = not open_space
        loc_id = loc_id & (loc_id - 1)
    return open_space


spaces_to_process: List[Tuple[int, int]] = [(1, 1)]
spaces_seen: Dict[Tuple[int, int], Tuple[int, int]] = {(1, 1): None}


def get_path_from_start(node):
    path = []
    while spaces_seen[node] is not None:
        path.append(node)
        node = spaces_seen[node]
    return path


while len(spaces_to_process) > 0:
    to_process = spaces_to_process.pop(0)
    neighbors = [(to_process[0], to_process[1] + 1), (to_process[0] + 1, to_process[1])]
    if to_process[0] > 0:
        neighbors.append((to_process[0] - 1, to_process[1]))
    if to_process[1] > 0:
        neighbors.append((to_process[0], to_process[1] - 1))

    for n in neighbors:
        if n not in spaces_seen:
            if is_open(n[0], n[1]):
                spaces_seen[n] = to_process
                if n == TARGET:
                    path: List[Tuple[int, int]] = get_path_from_start(n)
                    print(len(path))
                    exit(0)
                else:
                    spaces_to_process.append(n)
