from adventofcode import AoC


def part1(inp: list[str]):
    start = (0, 0)
    corners = [start]
    length = 0
    for line in inp:
        direction, steps, color = line.split(" ")
        steps = int(steps)
        length += steps
        if direction == "R":
            start = (start[0] + steps, start[1])
        elif direction == "L":
            start = (start[0] - steps, start[1])
        elif direction == "U":
            start = (start[0], start[1] + steps)
        elif direction == "D":
            start = (start[0], start[1] - steps)
        corners.append(start)

    shoelace_area = abs(
        sum(
            (v1[0] + v2[0]) * (v1[1] - v2[1]) / 2
            for v1, v2 in zip(corners, corners[1:])
        )
    )
    return int(shoelace_area + length / 2 + 1)


def part2(inp: list[str]):
    start = (0, 0)
    corners = [start]
    length = 0
    for line in inp:
        _, _, color = line.split(" ")
        steps = int(color[2:-2], 16)
        direction = color[-2]
        length += steps
        if direction == "0":
            start = (start[0] + steps, start[1])
        elif direction == "2":
            start = (start[0] - steps, start[1])
        elif direction == "3":
            start = (start[0], start[1] + steps)
        elif direction == "1":
            start = (start[0], start[1] - steps)
        corners.append(start)

    shoelace_area = abs(
        sum(
            (v1[0] + v2[0]) * (v1[1] - v2[1]) / 2
            for v1, v2 in zip(corners, corners[1:])
        )
    )
    return int(shoelace_area + length / 2 + 1)


aoc = AoC(part_1=part1, part_2=part2)
inp = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
aoc.assert_p1(inp, 62)
aoc.submit_p1()

aoc.assert_p2(inp, 952408144115)
aoc.submit_p2()
