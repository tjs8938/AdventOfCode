from src.AoC_2020.Utility.GameCodeComputer import GameCodeComputer

input_file = open("input.txt")
# input_file = open("test1.txt")

input_lines = input_file.read().splitlines()

game = GameCodeComputer(input_lines)

executed_instructions = set()


def debug_instruction(value):
    if game.inst_ptr in executed_instructions:
        print(game.accumulator)
        exit(0)

    executed_instructions.add(game.inst_ptr)


game.debug_func = debug_instruction
game.run()