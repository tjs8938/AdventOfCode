import json
import time
from pprint import pprint

with open("leaderboard.json") as leaderboard:
    data = json.load(leaderboard)

timestamps = {}

for member in data["members"].values():
    name = member["name"]
    # print(name)
    for day, puzzle in member["completion_day_level"].items():
        for p, ts in puzzle.items():
            # print(day, p, ts)
            timestamps.setdefault(str.zfill(day, 2), {}).setdefault(p, []).append((name, ts['get_star_ts']))

for day in timestamps.values():
    for puzzle in day.values():
        puzzle.sort(key=lambda x: x[1])

        for i in range(len(puzzle)):
            name = puzzle[i][0]
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(puzzle[i][1]))
            puzzle[i] = (name, time_str)

pprint(timestamps)
