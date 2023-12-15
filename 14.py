from textwrap import dedent

from adventofcode import AoC


def part1(inp: list[str]):
    grid = {}
    rocks = []
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            grid[(i, j)] = c
            if c == "O":
                rocks.append((i, j))
    for rock in rocks:
        x, y = rock
        while grid.get((x, y - 1)) == ".":
            grid[(x, y - 1)] = "O"
            grid[(x, y)] = "."
            y -= 1

    res = 0
    for j in range(len(inp)):
        res += (len(inp) - j) * sum(
            1 for i in range(len(inp[j])) if grid.get((i, j)) == "O"
        )
    return res


def get_hashable(grid):
    return tuple(grid.items())


def get_score(grid, inp):
    res = 0
    for j in range(len(inp)):
        res += (len(inp) - j) * sum(
            1 for i in range(len(inp[j])) if grid.get((i, j)) == "O"
        )
    return res


def print_grid(grid, inp):
    for j in range(len(inp)):
        print("".join(grid.get((i, j)) for i in range(len(inp[j]))))
    print()


def part2(inp: list[str]):
    grid = {}
    rocks = []
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            grid[(i, j)] = c
            if c == "O":
                rocks.append((i, j))
    seen_cycles = {get_hashable(grid)}
    cycles = [get_score(grid, inp)]
    cycle_hashes = []
    while True:
        # NORTH
        rocks = sorted(rocks, key=lambda r: r[1])
        new_rocks = []
        for rock in rocks:
            x, y = rock
            while grid.get((x, y - 1)) == ".":
                grid[(x, y - 1)] = "O"
                grid[(x, y)] = "."
                y -= 1
            new_rocks.append((x, y))
        rocks = new_rocks

        # WEST
        new_rocks = []
        rocks = sorted(rocks, key=lambda r: r[0])
        for rock in rocks:
            x, y = rock
            while grid.get((x - 1, y)) == ".":
                grid[(x - 1, y)] = "O"
                grid[(x, y)] = "."
                x -= 1
            new_rocks.append((x, y))
        rocks = new_rocks

        # SOUTH
        new_rocks = []
        rocks = sorted(rocks, key=lambda r: r[1], reverse=True)
        for rock in rocks:
            x, y = rock
            while grid.get((x, y + 1)) == ".":
                grid[(x, y + 1)] = "O"
                grid[(x, y)] = "."
                y += 1
            new_rocks.append((x, y))
        rocks = new_rocks

        # EAST
        new_rocks = []
        rocks = sorted(rocks, key=lambda r: r[0], reverse=True)
        for rock in rocks:
            x, y = rock
            while grid.get((x + 1, y)) == ".":
                grid[(x + 1, y)] = "O"
                grid[(x, y)] = "."
                x += 1
            new_rocks.append((x, y))
        rocks = new_rocks

        hashable = get_hashable(grid)
        if hashable in seen_cycles:
            idx_of_repeat = cycle_hashes.index(hashable)
            reptead_cycles = cycles[idx_of_repeat:]
            res_index = (1000000000 - idx_of_repeat) % len(reptead_cycles)
            return reptead_cycles[res_index]

        seen_cycles.add(hashable)
        cycles.append(get_score(grid, inp))
        cycle_hashes.append(hashable)


aoc = AoC(part_1=part1, part_2=part2)
aoc.assert_p1(
    """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""",
    136,
)
aoc.submit_p1()
aoc.assert_p2(
    """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""",
    63,
)
aoc.submit_p2()
