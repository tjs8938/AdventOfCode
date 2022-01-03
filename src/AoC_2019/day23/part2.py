import csv

from src.AoC_2019.day23.DataPacketBuffer import DataPacketBuffer
from src.AoC_2019.day23.NAT import NAT
from src.Utility.NonBlockingThreadedIntCodeComputer import NonBlockingThreadedIntCodeComputer


nat = None


def route_packet(dest, x, y):
    if dest == 255:
        nat.receive_packet(x, y)
    else:
        computers[dest].post_inputs([x, y])


file = open('input.txt')

tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

computers = []


for i in range(0, 50):
    comp = NonBlockingThreadedIntCodeComputer(tape.copy())
    buffer = DataPacketBuffer(route_packet)
    comp.out_func = buffer.receive_input
    comp.post_input(i)
    computers.append(comp)

nat = NAT(computers)

for i in range(0, 50):
    computers[i].start()

nat.monitor()
