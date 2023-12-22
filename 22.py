import dataclasses

from adventofcode import AoC


@dataclasses.dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)


@dataclasses.dataclass
class Brick:
    index: int
    start: Point
    end: Point


def parse_inp(inp: list[str]):
    for i, line in enumerate(inp):
        start, end = line.split("~")
        start = Point(*map(int, start.split(",")))
        end = Point(*map(int, end.split(",")))
        yield Brick(i, start, end)


def fall(bricks: list[Brick]):
    sorted_bricks = sorted(bricks, key=lambda brick: brick.start.z)
    landed = {}
    supports = {i: [] for i, _ in enumerate(sorted_bricks)}
    supported_by = {i: [] for i, _ in enumerate(sorted_bricks)}
    for brick in sorted_bricks:
        supporters = list()
        while brick.start.z > 1:
            for x in range(brick.start.x, brick.end.x + 1):
                for y in range(brick.start.y, brick.end.y + 1):
                    for z in range(brick.start.z, brick.end.z + 1):
                        if (supporter := (x, y, z - 1)) in landed:
                            supporters.append(supporter)
            if supporters:
                break

            brick.start += Point(0, 0, -1)
            brick.end += Point(0, 0, -1)

        for x in range(brick.start.x, brick.end.x + 1):
            for y in range(brick.start.y, brick.end.y + 1):
                for z in range(brick.start.z, brick.end.z + 1):
                    landed[(x, y, z)] = brick.index

        for supporter_index in set(landed[supporter] for supporter in supporters):
            supports[supporter_index].append(brick.index)
            supported_by[brick.index].append(supporter_index)
    return supports, supported_by


def part1(inp: list[str]):
    bricks = list(parse_inp(inp))
    supports, supported_by = fall(bricks)
    count = 0
    for i in supports:
        for j in supports[i]:
            if len(supported_by[j]) == 1:
                break
        else:
            count += 1
    return count


def part2(inp: list[str]):
    bricks = list(parse_inp(inp))
    supports, supported_by = fall(bricks)
    count = 0
    for i in supports:
        check = supports[i].copy()
        falls = {i}

        while check:
            curr = check.pop()
            if all(s in falls for s in supported_by[curr]):
                falls.add(curr)
                check += supports[curr]

        count += len(falls) - 1
    return count


aoc = AoC(part_1=part1, part_2=part2)
inp = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


aoc.assert_p1(inp, 5)
aoc.submit_p1()

aoc.assert_p2(inp, 7)
aoc.submit_p2()
