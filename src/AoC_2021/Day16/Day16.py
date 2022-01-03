from __future__ import annotations

from dataclasses import dataclass, field
from functools import reduce
from typing import List

from src.aoc_frame import run_part


def hex_to_bin(hex_str: str) -> str:
    output = ''
    words = [hex_str[i:i+8] for i in range(0, len(hex_str), 8)]
    for w in words:
        output += bin(int(w, 16))[2:].zfill(len(w)*4)

    return output


@dataclass
class Packet:
    version: int = 0
    type: int = 0
    value: int = 0
    sub_packets: List[Packet] = field(default_factory=list)

    def version_sum(self) -> int:
        return self.version + sum(map(lambda x: x.version_sum(), self.sub_packets))

    def get_value(self):
        sub_values = list(map(lambda x: x.get_value(), self.sub_packets))
        if self.type == 0:
            return sum(sub_values)
        if self.type == 1:
            return reduce(lambda x, y: x * y, sub_values, 1)
        if self.type == 2:
            return min(sub_values)
        if self.type == 3:
            return max(sub_values)
        if self.type == 4:
            return self.value
        if self.type == 5:
            return 1 if sub_values[0] > sub_values[1] else 0
        if self.type == 6:
            return 1 if sub_values[0] < sub_values[1] else 0
        if self.type == 7:
            return 1 if sub_values[0] == sub_values[1] else 0


@dataclass
class BinEncoding:
    str_rep: str
    index: int = 0

    def read_bits(self, num_bits) -> str:
        output = self.str_rep[self.index:self.index + num_bits]
        self.index += num_bits
        return output


def parse_packet(packet_bin):
    p = Packet()
    p.version = int(packet_bin.read_bits(3), 2)
    type_bits = packet_bin.read_bits(3)
    p.type = int(type_bits, 2)
    if p.type == 4:
        value_str = ''
        prefix = packet_bin.read_bits(1)
        read_more = True
        while read_more:
            value_str += packet_bin.read_bits(4)
            if prefix == '0':
                read_more = False
            else:
                prefix = packet_bin.read_bits(1)
        p.value = int(value_str, 2)
    else:
        length_type = packet_bin.read_bits(1)
        expected_packets = -1
        expected_bits = -1
        if length_type == '0':
            expected_bits = int(packet_bin.read_bits(15), 2) + packet_bin.index
        else:
            expected_packets = int(packet_bin.read_bits(11), 2)

        read_more_packets = True
        while read_more_packets:
            sub_packet = parse_packet(packet_bin)
            p.sub_packets.append(sub_packet)
            read_more_packets = (expected_packets == -1 or len(p.sub_packets) < expected_packets) and \
                                (expected_bits == -1 or packet_bin.index < expected_bits)

    return p


def part_a(input_data: str) -> str:
    bin_input = hex_to_bin(input_data)

    packet_bin = BinEncoding(bin_input)

    packet = parse_packet(packet_bin)

    return str(packet.version_sum())


def part_b(input_data: str) -> str:
    bin_input = hex_to_bin(input_data)

    packet_bin = BinEncoding(bin_input)

    packet = parse_packet(packet_bin)

    return str(packet.get_value())


# run_part(part_a, 'a', 2021, 16)
run_part(part_b, 'b', 2021, 16)

