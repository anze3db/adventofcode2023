from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def part1(inp: list[str]):
    res = 0
    for line in inp:
        winning, mine = line.split(": ")[1].split(" | ")
        winning = set(map(int, winning.split()))
        mine = set(map(int, mine.split()))
        if winning.intersection(mine):
            res += 2 ** (len(winning.intersection(mine)) - 1)
    return res


def part2(inp: list[str]):
    cards = {}
    for i, line in enumerate(inp):
        winning, mine = line.split(": ")[1].split(" | ")
        winning = set(map(int, winning.split()))
        mine = set(map(int, mine.split()))
        matches = winning.intersection(mine)
        cards[i] = cards.get(i, 1)
        for j in range(len(matches)):
            cards[i + j + 1] = cards.get(i + j + 1, 1) + cards.get(i, 1)
    return sum(cards.values())


assert (
    part1(
        dedent(
            """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
        ).splitlines()
    )
    == 13
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
        ).splitlines()
    )
    == 30
)
aoc.submit_p2(part2(aoc.get_input()))
