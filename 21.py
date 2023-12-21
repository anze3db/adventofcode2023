from collections import defaultdict

from adventofcode import AoC


def part1(inp: list[str]):
    if len(inp) < 20:
        steps = 6
    else:
        steps = 64

    grid = {}
    positions = set()
    for j, line in enumerate(inp):
        for i, char in enumerate(line):
            if char == "S":
                positions.add((i, j))
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = char

    for _ in range(steps):
        new_positions = set()
        for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            for position in positions:
                new_position = (position[0] + direction[0], position[1] + direction[1])
                if grid[new_position] == ".":
                    new_positions.add(new_position)
        positions = new_positions

    return len(positions)


def part2(inp: list[str]):
    grid = {}
    size = len(inp)
    positions: dict[int, set[tuple[int, int]]] = defaultdict(set)
    for j, line in enumerate(inp):
        for i, char in enumerate(line):
            if char == "S":
                positions[0].add((i, j))
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = char

    params = []
    for step in range(steps):
        for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            for position in positions[step]:
                new_position = (
                    (position[0] + direction[0]) % size,
                    (position[1] + direction[1]) % size,
                )
                new_position_real = (
                    (position[0] + direction[0]),
                    (position[1] + direction[1]),
                )
                if grid[new_position] == ".":
                    positions[step + 1].add(new_position_real)
        if step % size == steps % size:
            params.append(len(positions[step]))
        if len(params) == 3:
            break

    b0 = params[0]
    b1 = params[1] - params[0]
    b2 = params[2] - params[1]
    n = steps // len(inp)
    return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)


aoc = AoC(part_1=part1, part_2=part2)
inp = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

steps = 6
aoc.assert_p1(inp, 16)

steps = 64
aoc.submit_p1()

steps = 26501365
aoc.submit_p2()
