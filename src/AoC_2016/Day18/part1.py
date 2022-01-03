from typing import List

from src.Utility.MatrixPrint import print_matrix


def count_safe_spaces(start_row: str, row_count: int) -> int:
    grid: List[List[str]] = [list(start_row)]
    for i in range(1, row_count):
        new_row = []
        for x in range(len(grid[0])):
            left_above = '.' if x == 0 else grid[i-1][x-1]
            right_above = '.' if x == len(grid[0]) - 1 else grid[i-1][x+1]
            new_row.append('.' if left_above == right_above else '^')

        grid.append(new_row)

    # print_matrix(grid)
    safe_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '.':
                safe_count += 1
    return safe_count


assert(count_safe_spaces('.^^.^.^^^^', 10) == 38)
print(count_safe_spaces('.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....', 40))
print(count_safe_spaces('.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....', 400000))
