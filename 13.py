from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def find_equals(sets: list[set[tuple[int, str]]]):
    for i in range(len(sets) - 1):
        j = 0
        while i - j >= 0 and i + j + 1 < len(sets):
            if sets[i - j] != sets[i + j + 1]:
                break
            j += 1
        else:
            return i + 1


def part1(inp):
    patterns = "\n".join(inp).split("\n\n")
    res = 0
    for pattern in patterns:
        rows: list[set[tuple[int, str]]] = []
        for row in pattern.splitlines():
            rset = set()
            for i, r in enumerate(row):
                rset.add((i, r))
            rows.append(rset)
        if (r_res := find_equals(rows)) is not None:
            res += 100 * r_res
            continue

        cols: list[set[tuple[int, str]]] = []
        for col in zip(*pattern.splitlines()):
            cset = set()
            for i, c in enumerate(col):
                cset.add((i, c))
            cols.append(cset)
        if (c_res := find_equals(cols)) is not None:
            res += c_res
            continue
    return res


def find_equals_smudge(sets: list[set[tuple[int, str]]]):
    for i in range(len(sets) - 1):
        j = 0
        smudge_used = False
        while i - j >= 0 and i + j + 1 < len(sets):
            if len(diff := sets[i - j].difference(sets[i + j + 1])) > 1:
                break
            elif len(diff) == 1:
                if smudge_used:
                    break
                smudge_used = True
            j += 1
        else:
            if not smudge_used:
                continue
            return i + 1


def part2(inp):
    patterns = "\n".join(inp).split("\n\n")
    res = 0
    for pattern in patterns:
        rows: list[set[tuple[int, str]]] = []
        for row in pattern.splitlines():
            rset = set()
            for i, r in enumerate(row):
                rset.add((i, r))
            rows.append(rset)
        if (r_res := find_equals_smudge(rows)) is not None:
            res += 100 * r_res
            continue

        cols: list[set[tuple[int, str]]] = []
        for col in zip(*pattern.splitlines()):
            cset = set()
            for i, c in enumerate(col):
                cset.add((i, c))
            cols.append(cset)
        if (c_res := find_equals_smudge(cols)) is not None:
            res += c_res
            continue
    return res


assert (
    part1(
        dedent(
            """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
        ).splitlines()
    )
    == 405
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
        ).splitlines()
    )
    == 400
)
aoc.submit_p2(part2(aoc.get_input()))
