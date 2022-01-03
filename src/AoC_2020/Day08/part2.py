from src.AoC_2020.Utility.GameCodeComputer import GameCodeComputer

input_file = open("input.txt")
# input_file = open("test1.txt")

input_lines = input_file.read().splitlines()


def debug_instruction(value):
    if game.inst_ptr in executed_instructions:
        # print(game.accumulator)
        return -1

    executed_instructions.add(game.inst_ptr)
    return 0


for i in range(0, len(input_lines)):

    code = input_lines.copy()
    if code[i].count("jmp") > 0:
        code[i] = code[i].replace("jmp", "nop")
    elif code[i].count("nop") > 0:
        code[i] = code[i].replace("nop", "jmp")
    else:
        continue

    game = GameCodeComputer(code)
    executed_instructions = set()

    game.debug_func = debug_instruction
    val = game.run()
    if val != -1:
        print(val)
        break
