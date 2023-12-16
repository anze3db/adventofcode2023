from adventofcode import AoC


def print_grid(grid: dict[tuple[int, int], str], seen: set[tuple[int, int]]):
    min_x = min(x for x, _ in grid.keys())
    max_x = max(x for x, _ in grid.keys())
    min_y = min(y for _, y in grid.keys())
    max_y = max(y for _, y in grid.keys())
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in seen:
                print("#", end="")
            else:
                print(grid[(x, y)], end="")
        print()


def walk_grid(
    grid: dict[tuple[int, int], str],
    start: tuple[int, int],
    direction: tuple[int, int] = (1, 0),
    seen=None,
    seen_with_dir=None,
):
    pos = start
    if seen is None:
        seen = set()
    if seen_with_dir is None:
        seen_with_dir = set()

    while True:
        if (pos, direction) in seen_with_dir:
            break
        seen.add(pos)
        seen_with_dir.add((pos, direction))
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        # print_grid(grid, seen)
        if next_pos not in grid:
            break
        if grid[next_pos] == ".":
            pos = next_pos
            continue
        if grid[next_pos] == "|":
            if direction[0] != 0:
                return walk_grid(
                    grid, next_pos, (0, 1), seen, seen_with_dir
                ) | walk_grid(grid, next_pos, (0, -1), seen, seen_with_dir)
            else:
                pos = next_pos
                continue
        if grid[next_pos] == "-":
            if direction[1] != 0:
                return walk_grid(
                    grid, next_pos, (1, 0), seen, seen_with_dir
                ) | walk_grid(grid, next_pos, (-1, 0), seen, seen_with_dir)
            else:
                pos = next_pos
                continue
        if grid[next_pos] == "/":
            if direction[0] != 0:
                direction = (0, -direction[0])
            else:
                direction = (-direction[1], 0)
            pos = next_pos
            continue
        if grid[next_pos] == "\\":
            if direction[0] != 0:
                direction = (0, direction[0])
            else:
                direction = (direction[1], 0)
            pos = next_pos
            continue
    return seen


def part1(inp: list[str]):
    grid = {}
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            grid[(i, j)] = c
    seen = walk_grid(grid, (-1, 0))
    return len(seen) - 1


def part2(inp: list[str]):
    grid = {}
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            grid[(i, j)] = c

    min_x = min(x for x, _ in grid.keys())
    max_x = max(x for x, _ in grid.keys())
    min_y = min(y for _, y in grid.keys())
    max_y = max(y for _, y in grid.keys())

    res = 0
    res = max(res, len(walk_grid(grid, (0, min_y), (1, 0))))
    res = max(res, len(walk_grid(grid, (0, max_y), (-1, 0))))
    res = max(res, len(walk_grid(grid, (min_x, 0), (0, 1))))
    res = max(res, len(walk_grid(grid, (max_x, 0), (0, -1))))
    for i in range(0, max_y + 1):
        res = max(res, len(walk_grid(grid, (i, min_y), (0, 1))))
        res = max(res, len(walk_grid(grid, (i, max_y), (0, -1))))
    for i in range(0, max_x + 1):
        res = max(res, len(walk_grid(grid, (min_x, i), (1, 0))))
        res = max(res, len(walk_grid(grid, (max_x, i), (-1, 0))))

    return res


aoc = AoC(part_1=part1, part_2=part2)
inp = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
aoc.assert_p1(inp, 46)
aoc.submit_p1()

aoc.assert_p2(inp, 51)
aoc.submit_p2()
