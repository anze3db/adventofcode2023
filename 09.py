from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def part1(inp):
    res = 0
    for line in inp:
        nums = list(map(int, line.split()))
        layers = [nums]
        curr_layer = nums
        while not layers or set(layers[-1]) != set([0]):
            layers.append(
                [curr_layer[i + 1] - curr_layer[i] for i in range(len(curr_layer) - 1)]
            )
            curr_layer = layers[-1]

        for i in range(len(layers) - 2, -1, -1):
            if i == 0:
                res += layers[i][-1] + layers[i + 1][-1]

            layers[i].append(layers[i][-1] + layers[i + 1][-1])
    return res


def part2(inp):
    res = 0
    for line in inp:
        nums = list(map(int, line.split()))
        layers = [nums]
        curr_layer = nums
        while not layers or set(layers[-1]) != set([0]):
            layers.append(
                [curr_layer[i + 1] - curr_layer[i] for i in range(len(curr_layer) - 1)]
            )
            curr_layer = layers[-1]

        for i in range(len(layers) - 2, -1, -1):
            nex = layers[i][0] - layers[i + 1][0]
            if i == 0:
                res += nex

            layers[i] = [nex] + layers[i]
    return res


assert (
    part1(
        dedent(
            """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
        ).splitlines()
    )
    == 114
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
        ).splitlines()
    )
    == 2
)
aoc.submit_p2(part2(aoc.get_input()))
