# aoc_day_16.py

from __future__ import annotations
import operator
from functools import reduce
from dataclasses import dataclass, field
from solution.aoc_base import AocBaseClass


@dataclass
class LiteralPacket:
    version: int
    type: int
    value: int
    size: int


@dataclass
class OperatorPacket:
    version: int
    type: int
    mode: int
    packets: list[OperatorPacket | LiteralPacket] = field(default_factory=list)

    @property
    def size(self):
        return sum(p.size for p in self.packets) + (18 if self.mode else 22)


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return bin(int(puzzle_input, 16))[2:].zfill(len(puzzle_input) * 4)

    DAY = 16

    def decode(self, bits):
        version = int(bits[:3], 2)
        type_ = int(bits[3:6], 2)

        payload = bits[6:]

        if type_ == 4:
            size = 6
            number = ""
            while payload:
                more = int(payload[0])
                number += payload[1:5]
                size += 5
                if not more:
                    break
                payload = payload[5:]
            return LiteralPacket(version, type_, int(number, 2), size)
        else:
            mode = int(payload[0])
            sub_packets = []
            if mode:
                sub_packet_count = int(payload[1:12], 2)
                sub_packet_bits = payload[12:]
                while len(sub_packets) < sub_packet_count:
                    sub_packets.append(self.decode(sub_packet_bits))
                    sub_packet_bits = sub_packet_bits[sub_packets[-1].size :]
            else:
                sub_packet_size = int(payload[1:16], 2)
                sub_packet_bits = payload[16:]
                while sum(p.size for p in sub_packets) < sub_packet_size:
                    sub_packets.append(self.decode(sub_packet_bits))
                    sub_packet_bits = sub_packet_bits[sub_packets[-1].size :]
            return OperatorPacket(
                version,
                type_,
                mode,
                sub_packets,
            )

    def version_sum(self, packet):
        if isinstance(packet, LiteralPacket):
            return packet.version

        return packet.version + sum(self.version_sum(p) for p in packet.packets)

    def visit(self, packet):
        if isinstance(packet, LiteralPacket):
            return packet.value

        return {
            0: lambda packet_: sum(self.visit(p) for p in packet_.packets),
            1: lambda packet_: reduce(
                operator.mul, (self.visit(p) for p in packet_.packets)
            ),
            2: lambda packet_: min(self.visit(p) for p in packet_.packets),
            3: lambda packet_: max(self.visit(p) for p in packet_.packets),
            5: lambda packet_: int(
                self.visit(packet_.packets[0]) > self.visit(packet_.packets[1])
            ),
            6: lambda packet_: int(
                self.visit(packet_.packets[0]) < self.visit(packet_.packets[1])
            ),
            7: lambda packet_: int(
                self.visit(packet_.packets[0]) == self.visit(packet_.packets[1])
            ),
        }[packet.type](packet)

    def part1(self):
        """Solve part 1"""
        return self.version_sum(self.decode(self.data))

    def part2(self):
        """Solve part 2"""
        return self.visit(self.decode(self.data))


if __name__ == "__main__":
    AocSolution().print_solution()
