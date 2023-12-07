from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def part1(inp):
    times = list(map(int, inp[0].split(": ")[1].split()))
    distances = list(map(int, inp[1].split(": ")[1].split()))
    num = 1
    for time, distance in zip(times, distances):
        options = 0
        for i in range(1, time):
            if (time - i) * i > distance:
                options += 1
        num *= options
    return num


def part2(inp):
    time = int(inp[0].split(": ")[1].replace(" ", ""))
    distance = int(inp[1].split(": ")[1].replace(" ", ""))

    num = 0
    for i in range(1, time):
        if (time - i) * i > distance:
            num += 1
    return num


assert (
    part1(
        dedent(
            """Time:      7  15   30
Distance:  9  40  200"""
        ).splitlines()
    )
    == 288
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """Time:      7  15   30
Distance:  9  40  200"""
        ).splitlines()
    )
    == 71503
)
aoc.submit_p2(part2(aoc.get_input()))
