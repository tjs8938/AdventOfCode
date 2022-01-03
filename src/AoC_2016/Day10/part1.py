import re
from typing import Callable, List, Dict, Tuple

pattern = re.compile(
    "(bot|value) (\d+) (goes to bot (\d+)|gives low to (bot|output) (\d+) and high to (bot|output) (\d+))")

comparators: Dict[Tuple[int, int], int] = {}


class Bot:

    def __init__(self, bot_num):
        self.bot_num = bot_num
        self.low: Callable = None
        self.high: Callable = None
        self.chips: List[int] = []

    def take_chip(self, chip: int):
        self.chips.append(chip)
        self.process_chips()

    def process_chips(self):
        while len(self.chips) >= 2 and self.low is not None and self.high is not None:
            h = max(self.chips[:2])
            l = min(self.chips[:2])
            self.chips = self.chips[2:]
            self.low(l)
            self.high(h)
            comparators[(l, h)] = self.bot_num

    def __repr__(self):
        return str(self.bot_num)


def process_bots(filename: str):
    all_bots: Dict[int, Bot] = {}
    outputs: Dict[int, List[int]] = {}

    def get_bot(num: int) -> Bot:
        return all_bots.setdefault(num, Bot(num))

    class Outputter:

        def __init__(self, bin):
            self.bin = bin

        def pass_output(self, value: int):
            outputs.setdefault(self.bin, [])
            outputs[self.bin].append(value)

    for line in open(filename).read().splitlines():
        match = pattern.match(line)
        if match.group(1) == "value":
            bot_num = int(match.group(4))
            chip_num = int(match.group(2))
            get_bot(bot_num).take_chip(chip_num)
        else:
            bot_num = int(match.group(2))
            low_command = match.group(5)
            low_value = int(match.group(6))
            high_command = match.group(7)
            high_value = int(match.group(8))

            bot = get_bot(bot_num)
            if low_command == 'bot':
                bot.low = get_bot(low_value).take_chip
            else:
                outputter = Outputter(low_value)
                bot.low = outputter.pass_output

            if high_command == 'bot':
                bot.high = get_bot(high_value).take_chip
            else:
                outputter = Outputter(high_value)
                bot.high = outputter.pass_output

    for bot in all_bots.values():
        bot.process_chips()
        if len(bot.chips) > 0:
            print(bot.bot_num)

    # print(outputs)
    # print(all_bots)
    return outputs


outputs = process_bots("input.txt")
print(comparators[(17, 61)])
print(outputs[0][0] * outputs[1][0] * outputs[2][0])
