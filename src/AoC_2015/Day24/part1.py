from copy import copy
from functools import reduce
from heapq import heappush
from typing import List

from src.AoC_2015.Day24.Package import Package

# filename = "test1.txt"
filename = "input.txt"


file = open(filename)
present_weights = list(map(lambda x: int(x), file.read().splitlines()))


presents = {}
for i in range(len(present_weights)):
    presents[str(pow(2, i))] = present_weights[i]
    presents[str(0 - pow(2, i))] = present_weights[i]
# print(presents)
target = reduce(lambda a, b: a+b, presents.values())/6


def gray(n: int) -> int:
    return n ^ (n >> 1)


# Test Data
right_sum = []
rolling_sum = 0
for i in range(1, pow(2, len(present_weights))):
    # print("{:05b} - {:05b} = {}".format(gray(i), gray(i - 1), gray(i) - gray(i - 1)))
    toggle = gray(i) - gray(i - 1)
    amount = presents[str(toggle)]
    if toggle > 0:
        rolling_sum += amount
    else:
        rolling_sum -= amount
    if rolling_sum == target:
        right_sum.append(gray(i))

# print(right_sum)

left_to_process = copy(right_sum)
confirmed_groups = set()

while len(left_to_process) > 0:
    search_num = left_to_process.pop()
    for candidate in right_sum:
        if candidate & search_num == 0:
            found_complement = True
            third_complement = pow(2, len(present_weights)) - 1 - search_num - candidate
            confirmed_groups.add(search_num)
            confirmed_groups.add(candidate)
            confirmed_groups.add(third_complement)

            if candidate in left_to_process:
                left_to_process.remove(candidate)
            if third_complement in left_to_process:
                left_to_process.remove(third_complement)
            break


# print(confirmed_groups)
package_groups: List[Package] = []

for i in confirmed_groups:
    heappush(package_groups, Package(i, present_weights))

print(package_groups[0].quantum_entanglement)
