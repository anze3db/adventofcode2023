from textwrap import dedent

from utils import AoC

aoc = AoC()


def part1(inp):
    grid = {}
    directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)}
    res = 0

    processed = set()
    symbols = set()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if not c.isnumeric() and c != ".":
                symbols.add(c)

    for x, y in grid:
        if grid[(x, y)].isnumeric():
            if (x, y) in processed:
                continue
            processed.add((x, y))
            xs = [x]
            x2 = x + 1
            num = grid[(x, y)]
            while grid.get((x2, y), "").isnumeric():
                processed.add((x2, y))
                num += grid[(x2, y)]
                xs.append(x2)
                x2 += 1
            for x in xs:
                for direction in directions:
                    if grid.get((x + direction[0], y + direction[1])) in symbols:
                        res += int(num)
                        break
                else:
                    continue
                break

    return res


def part2(inp):
    grid = {}
    directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)}
    res = 0
    symbols = set()

    processed = set()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if not c.isnumeric() and c != ".":
                symbols.add(c)

    for x, y in grid:
        if grid[(x, y)].isnumeric():
            if (x, y) in processed:
                continue
            processed.add((x, y))
            xs = [x]
            x2 = x + 1
            num = grid[(x, y)]
            while grid.get((x2, y), "").isnumeric():
                processed.add((x2, y))
                num += grid[(x2, y)]
                xs.append(x2)
                x2 += 1
            for x in xs:
                for direction in directions:
                    starx, stary = x + direction[0], y + direction[1]
                    if grid.get((starx, stary)) == "*":
                        for direction2 in directions:
                            starxx, staryy = (
                                starx + direction2[0],
                                stary + direction2[1],
                            )
                            if starxx in xs and staryy == y:
                                # same number
                                continue
                            if grid.get((starxx, staryy), "").isnumeric():
                                # found another number
                                if (starxx, staryy) in processed:
                                    continue
                                num2 = grid[(starxx, staryy)]
                                processed.add((starxx, staryy))
                                for xoption in [starxx - 1, starxx - 2]:
                                    if grid.get((xoption, staryy), "").isnumeric():
                                        num2 = grid[(xoption, staryy)] + num2
                                        processed.add((xoption, staryy))
                                    else:
                                        break
                                for xoption in [starxx + 1, starxx + 2]:
                                    if grid.get((xoption, staryy), "").isnumeric():
                                        num2 = num2 + grid[(xoption, staryy)]
                                        processed.add((xoption, staryy))
                                    else:
                                        break
                                res += int(num) * int(num2)
                        break
                else:
                    continue
                break

    return res


assert (
    part1(
        dedent(
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
        ).splitlines()
    )
    == 4361
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
        ).splitlines()
    )
    == 467835
)
aoc.submit_p2(part2(aoc.get_input()))
