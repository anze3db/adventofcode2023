import math
from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def parse(inp):
    directions = "\n".join(inp).split("\n\n")[0]
    mp = "\n".join(inp).split("\n\n")[1]
    mapping = {}
    for line in mp.splitlines():
        key = line.split(" = ")[0]
        options = tuple(
            line.split(" = ")[1].replace("(", "").replace(")", "").strip().split(", ")
        )
        mapping[key] = options
    return directions, mapping


def part1(inp):
    directions, mapping = parse(inp)

    current = "AAA"
    res = 0
    while current != "ZZZ":
        next_index = 1 if directions[res % len(directions)] == "R" else 0
        res += 1
        current = mapping[current][next_index]
    return res


def part2(inp):
    directions, mapping = parse(inp)
    starts = list([m for m in mapping if m.endswith("A")])
    finishes = []

    for s in starts:
        current = s
        res = 0
        while not current.endswith("Z"):
            next_index = 1 if directions[res % len(directions)] == "R" else 0
            res += 1
            current = mapping[current][next_index]
        finishes.append(res)
    return math.lcm(*finishes)


assert (
    part1(
        dedent(
            """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
        ).splitlines()
    )
    == 6
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
        ).splitlines()
    )
    == 6
)
aoc.submit_p2(part2(aoc.get_input()))
