from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def part1(inp: list[str]):
    empty_lines = set()
    for i, line in enumerate(inp):
        if set(line) == {"."}:
            empty_lines.add(i)
    empty_columns = set()
    for i in range(len(inp[0])):
        if set(line[i] for line in inp) == {"."}:
            empty_columns.add(i)
    expanded_inp = []

    for j, line in enumerate(inp):
        if j in empty_lines:
            expanded_inp.append("." * len(expanded_inp[0]))
        curr = ""
        for i, column in enumerate(line):
            curr += column
            if i in empty_columns:
                curr += column
        expanded_inp.append(curr)

    galaxies = set()
    for j, line in enumerate(expanded_inp):
        for i, column in enumerate(line):
            if column == "#":
                galaxies.add((i, j))

    res = 0
    galaxies_lst = list(galaxies)
    for i, galaxy in enumerate(galaxies_lst):
        for galaxy_other in galaxies_lst[i + 1 :]:
            # Mangattan distances between galaxies:
            res += abs(galaxy[0] - galaxy_other[0]) + abs(galaxy[1] - galaxy_other[1])
    return res


def part2(inp, expansion=1000000):
    expansion -= 1  # offset for the row that already exists

    empty_lines = set()
    for i, line in enumerate(inp):
        if set(line) == {"."}:
            empty_lines.add(i)
    empty_columns = set()
    for i in range(len(inp[0])):
        if set(line[i] for line in inp) == {"."}:
            empty_columns.add(i)

    galaxies = set()

    cnt_rows = 0
    for j, line in enumerate(inp):
        cnt_cols = 0
        if j in empty_lines:
            cnt_rows += 1
        for i, column in enumerate(line):
            if i in empty_columns:
                cnt_cols += 1
            if column == "#":
                galaxies.add((i + expansion * cnt_cols, j + expansion * cnt_rows))

    res = 0
    galaxies_lst = list(galaxies)
    for i, galaxy in enumerate(galaxies_lst):
        for galaxy_other in galaxies_lst[i + 1 :]:
            # Mangattan distances between galaxies:
            res += abs(galaxy[0] - galaxy_other[0]) + abs(galaxy[1] - galaxy_other[1])
    return res


assert (
    part1(
        dedent(
            """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
        ).splitlines()
    )
    == 374
)
# aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
        ).splitlines(),
        2,
    )
    == 374
)

assert (
    part2(
        dedent(
            """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
        ).splitlines(),
        10,
    )
    == 1030
)
assert (
    part2(
        dedent(
            """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
        ).splitlines(),
        100,
    )
    == 8410
)
aoc.submit_p2(part2(aoc.get_input()))
