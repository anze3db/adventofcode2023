import sympy
from adventofcode import AoC


def part1(inp: list[str]):
    points = []
    for line in inp:
        p_start, p_end = line.split(" @ ")
        p_start = list(map(int, p_start.split(", ")))[:-1]
        p_vel = list(map(int, p_end.split(", ")))[:-1]
        points.append((p_start, p_vel))

    cnt = 0
    for i, line1 in enumerate(points):
        for j, line2 in enumerate(points):
            if j <= i:
                continue

            pos1, v1 = line1
            pos2, v2 = line2

            if v1[0] * v2[1] - v1[1] * v2[0] == 0:
                if v1[0] * (pos1[1] - pos2[1]) + v1[1] * (pos2[0] - pos1[0]) == 0:
                    cnt += 1
                continue
            t2 = (v1[0] * (pos1[1] - pos2[1]) + v1[1] * (pos2[0] - pos1[0])) / (
                v1[0] * v2[1] - v1[1] * v2[0]
            )
            t1 = (pos2[0] - pos1[0] + v2[0] * t2) / v1[0]
            if t1 < 0 or t2 < 0:
                continue
            intersection = pos2[0] + v2[0] * t2, pos2[1] + v2[1] * t2
            cnt += start <= intersection[0] <= end and start <= intersection[1] <= end
    return cnt


def find_stone_position(points):
    pos1, vel1 = points[0]
    pos2, vel2 = points[1]
    pos3, vel3 = points[2]
    p1, p2, p3, v1, v2, v3, t1, t2, t3 = sympy.symbols(
        "p1 p2 p3 v1 v2 v3 t1 t2 t3", real=True
    )
    equations = [
        sympy.Eq(p1 + v1 * t1, pos1[0] + vel1[0] * t1),
        sympy.Eq(p2 + v2 * t1, pos1[1] + vel1[1] * t1),
        sympy.Eq(p3 + v3 * t1, pos1[2] + vel1[2] * t1),
        sympy.Eq(p1 + v1 * t2, pos2[0] + vel2[0] * t2),
        sympy.Eq(p2 + v2 * t2, pos2[1] + vel2[1] * t2),
        sympy.Eq(p3 + v3 * t2, pos2[2] + vel2[2] * t2),
        sympy.Eq(p1 + v1 * t3, pos3[0] + vel3[0] * t3),
        sympy.Eq(p2 + v2 * t3, pos3[1] + vel3[1] * t3),
        sympy.Eq(p3 + v3 * t3, pos3[2] + vel3[2] * t3),
    ]
    solution = sympy.solve(equations)[0]
    return solution[p1], solution[p2], solution[p3]


def part2(inp: list[str]):
    points = []
    for line in inp:
        p_start, p_end = line.split(" @ ")
        p_start = list(map(int, p_start.split(", ")))
        p_vel = list(map(int, p_end.split(", ")))
        points.append((p_start, p_vel))
    return sum(find_stone_position(points))


aoc = AoC(part_1=part1, part_2=part2)
inp = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
start = 7
end = 27
aoc.assert_p1(inp, 2)
start = 200000000000000
end = 400000000000000
aoc.submit_p1()

aoc.assert_p2(inp, 47)
aoc.submit_p2()
