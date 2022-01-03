import itertools
from collections import defaultdict
from dataclasses import dataclass
from pprint import pprint
from typing import List, Dict, Tuple

from aocd.transforms import lines

from src.aoc_frame import run_part


@dataclass
class Die:
    rolls: int = 0
    index: int = 0

    def roll(self) -> int:
        self.rolls += 1
        self.index += 1
        return self.index


@dataclass
class Player:
    score: int = 0
    pos: int = 0


def part_a(input_data: str) -> str:
    in_lines = lines(input_data)
    players: List[Player] = []
    for l in in_lines:
        pos = int(l.split()[-1]) - 1
        players.append(Player(pos=pos))

    die = Die()
    step = 0
    while all(map(lambda x: x.score < 1000, players)):
        player = players[step]
        player.pos = (player.pos + die.roll() + die.roll() + die.roll()) % 10
        player.score += player.pos + 1
        step = (step + 1) % 2

    losing_score = min(map(lambda x: x.score, players))
    return str(losing_score * die.rolls)


def part_b(input_data: str) -> str:
    in_lines = lines(input_data)
    p1_pos = int(in_lines[0].split()[-1]) - 1
    p2_pos = int(in_lines[1].split()[-1]) - 1

    wins = [0, 0]
    turn = 0

    # Game state Tuple[p1 pos, p2 pos, p1 score, p2 score]
    games: Dict[Tuple[int, int, int, int], int] = defaultdict(int)
    games[p1_pos, p2_pos, 0, 0] = 1

    roll_map = defaultdict(int)
    for x, y, z in itertools.product(range(1, 4), repeat=3):
        roll_map[x + y + z] += 1

    while len(games) > 0:
        new_states: Dict[Tuple[int, int, int, int], int] = defaultdict(int)
        for state, count in games.items():
            p1_pos, p2_pos, p1_score, p2_score = state
            for roll, roll_count in roll_map.items():
                pos = state[turn]
                score = state[turn + 2]

                pos = (pos + roll) % 10
                score += pos + 1

                if score >= 21:
                    wins[turn] += count * roll_count
                else:
                    if turn == 0:
                        p1_pos = pos
                        p1_score = score
                    else:
                        p2_pos = pos
                        p2_score = score
                    new_states[(p1_pos, p2_pos, p1_score, p2_score)] += count * roll_count
        games = new_states
        turn = (turn + 1) % 2
        # pprint(games)

    return str(max(wins))


# run_part(part_a, 'a', 2021, 21)
run_part(part_b, 'b', 2021, 21)
