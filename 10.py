from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def neighbors(grid, x, y):
    current_shape = grid[x, y]
    steps = {
        "S": ((0, 1), (0, -1), (1, 0), (-1, 0)),
        "L": ((0, -1), (1, 0)),
        "J": ((0, -1), (-1, 0)),
        "F": ((0, 1), (1, 0)),
        "7": ((0, 1), (-1, 0)),
        "|": ((0, 1), (0, -1)),
        "-": ((1, 0), (-1, 0)),
    }
    options = {
        "S": {
            # x, y
            (0, 1): {"|", "J", "L"},
            (0, -1): {"|", "7", "F"},
            (1, 0): {"-", "J", "7"},
            (-1, 0): {"-", "F", "L"},
        },
        "L": {
            (0, -1): ("S", "|", "7", "F"),
            (1, 0): ("S", "-", "J", "7"),
        },
        "J": {
            (0, -1): ("S", "|", "7", "F"),
            (-1, 0): ("S", "-", "L", "F"),
        },
        "F": {
            (0, 1): ("S", "|", "J", "L"),
            (1, 0): ("S", "-", "J", "7"),
        },
        "7": {
            (0, 1): ("S", "|", "J", "L"),
            (-1, 0): ("S", "-", "L", "F"),
        },
        "|": {
            (0, -1): ("S", "|", "7", "F"),
            (0, 1): ("S", "|", "J", "L"),
        },
        "-": {
            (1, 0): ("S", "-", "7", "J"),
            (-1, 0): ("S", "-", "L", "F"),
        },
    }
    for dx, dy in options[current_shape].keys():
        if shape := grid.get((x + dx, y + dy)):
            if shape in options[current_shape][dx, dy]:
                yield x + dx, y + dy


def next_step(grid, x, y):
    for nx, ny in neighbors(grid, x, y):
        if grid[nx, ny] == "S":
            return nx, ny
    return None


def part1(inp: list[str]):
    grid = {}
    start = None
    weights = {}
    for j, line in enumerate(inp: list[str]):
        for i, c in enumerate(line):
            grid[i, j] = c
            if c == "S":
                start = i, j

    queue = []
    weights[start] = 0
    queue.append(start)
    while queue:
        x, y = queue.pop(0)
        for nx, ny in neighbors(grid, x, y):
            if (nx, ny) not in weights:
                weights[nx, ny] = weights[x, y] + 1
                queue.append((nx, ny))
    return max(weights.values())


def part2(inp: list[str]):
    grid = {}
    start = None
    weights = {}
    for j, line in enumerate(inp: list[str]):
        for i, c in enumerate(line):
            grid[i, j] = c
            if c == "S":
                start = i, j

    queue = []
    weights[start] = 0
    queue.append(start)
    while queue:
        x, y = queue.pop(0)
        for nx, ny in neighbors(grid, x, y):
            if (nx, ny) not in weights:
                weights[nx, ny] = weights[x, y] + 1
                queue.append((nx, ny))

    res = 0
    # I couldn't figure out how to do the flood fill, so I followed the following hint:
    # > I then just looked at every coordinate that ISN'T part of the loop,
    # > and counted how many times |, J, L, or S appear to the left of it.
    # > If it appears an odd number of times, the given coord MUST be in the loop.
    loop = {(x, y): c for (x, y), c in grid.items() if (x, y) in weights}
    min_x, max_x = min(weights)[0], max(weights)[0]
    min_y, max_y = min(s[1] for s in weights), max(s[1] for s in weights)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in loop:
                continue
            cnt = 0
            for _ in range(max_x):
                x -= 1
                if x < 0:
                    break
                if loop.get((x, y), "?") in "|JL":
                    cnt += 1
            res += cnt % 2
    return res


assert (
    part1(
        dedent(
            """.....
.S-7.
.|.|.
.L-J.
....."""
        ).splitlines()
    )
    == 4
)

assert (
    part1(
        dedent(
            """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
        ).splitlines()
    )
    == 8
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
        ).splitlines()
    )
    == 4
)
assert (
    part2(
        dedent(
            """...........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""
        ).splitlines()
    )
    == 4
)
assert (
    part2(
        dedent(
            """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
        ).splitlines()
    )
    == 10
)
aoc.submit_p2(part2(aoc.get_input()))
