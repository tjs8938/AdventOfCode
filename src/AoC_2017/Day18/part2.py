import threading

from src.AoC_2017.Day18.ThreadedDuetAssemblyComputer import ThreadedDuetAssemblyComputer

program_lines = open("input.txt").read().splitlines()

prog0 = ThreadedDuetAssemblyComputer(program_lines, 0)
prog1 = ThreadedDuetAssemblyComputer(program_lines, 1)

prog0.out_func = prog1.post_input
prog1.out_func = prog0.post_input

thread0 = threading.Thread(target=prog0.execute)
thread1 = threading.Thread(target=prog1.execute)

thread0.start()
thread1.start()