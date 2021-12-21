# aoc_day_21.py

import collections
import dataclasses
import functools
import itertools
from solution.aoc_base import AocBaseClass


class Dice:
    def __init__(self):
        self.generator = itertools.cycle(range(1, 101))
        self.rolls = 0

    def roll(self):
        self.rolls += 3
        return sum(next(self.generator) for _ in range(3))


@dataclasses.dataclass(frozen=True)
class Player:
    position: int
    score: int = 0

    def move(self, value):
        position = self.position + value
        position = (position % 10) + 10 * (position % 10 == 0)
        score = self.score + position
        return Player(position, score=score)


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return tuple(
            Player(int(player.split(" ")[-1])) for player in puzzle_input.splitlines()
        )

    DAY = 21

    @functools.cache
    def quantum_wins(self, player_1, player_2, current_player):
        win_counts = collections.Counter()

        for rolls in itertools.product([1, 2, 3], repeat=3):
            roll = sum(rolls)

            players = {1: player_1, 2: player_2}
            player = players[current_player].move(roll)
            players[current_player] = player

            if player.score >= 21:
                win_counts[current_player] += 1
            else:
                next_player = 3 - current_player
                win_counts.update(
                    self.quantum_wins(players[1], players[2], next_player)
                )

        return win_counts

    def part1(self):
        """Solve part 1"""
        player_1, player_2 = self.data
        dice = Dice()

        while True:
            player_1 = player_1.move(dice.roll())
            if player_1.score >= 1000:
                return player_2.score * dice.rolls
                break

            player_2 = player_2.move(dice.roll())
            if player_2.score >= 1000:
                return player_1.score * dice.rolls
                break

    def part2(self):
        """Solve part 2"""
        player_1, player_2 = self.data
        win_counts = self.quantum_wins(player_1, player_2, 1)
        return win_counts.most_common()[0][1]


if __name__ == "__main__":
    AocSolution().print_solution()
