import dataclasses
import heapq
import math
from collections import defaultdict

from adventofcode import AoC


@dataclasses.dataclass
class Option:
    pos: tuple[int, int]
    direction: tuple[int, int]
    direction_count: int

    def __lt__(self, other):
        return self.pos < other.pos

    def __hash__(self) -> int:
        return hash((self.pos, self.direction, self.direction_count))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def dijkstra(start, end, grid):
    visited = set()
    queue = [
        (grid[(1, 0)], Option((1, 0), (1, 0), 1)),
        (grid[(0, 1)], Option((0, 1), (0, 1), 1)),
    ]
    while queue:
        score, option = heapq.heappop(queue)
        if option.pos == end:
            return score

        if option in visited:
            continue

        visited.add(option)

        next_options = [
            Option(
                add(option.pos, (-option.direction[1], option.direction[0])),
                (-option.direction[1], option.direction[0]),
                1,
            ),
            Option(
                add(option.pos, (option.direction[1], -option.direction[0])),
                (option.direction[1], -option.direction[0]),
                1,
            ),
        ]
        if option.direction_count < 3:
            next_options.append(
                Option(
                    add(option.pos, option.direction),
                    option.direction,
                    option.direction_count + 1,
                )
            )

        for n in next_options:
            if n.pos not in grid:
                continue

            current_score = grid[n.pos] + score
            heapq.heappush(queue, (current_score, n))


def dijkstra2(start, end, grid):
    visited = set()
    queue = [
        (grid[(1, 0)], Option((1, 0), (1, 0), 1)),
        (grid[(0, 1)], Option((0, 1), (0, 1), 1)),
    ]
    while queue:
        score, option = heapq.heappop(queue)
        if option.pos == end and option.direction_count >= 4:
            return score

        if option in visited:
            continue

        visited.add(option)

        next_options = []
        if option.direction_count < 10:
            next_options.append(
                Option(
                    add(option.pos, option.direction),
                    option.direction,
                    option.direction_count + 1,
                )
            )

        if option.direction_count >= 4:
            next_options.append(
                Option(
                    add(option.pos, (-option.direction[1], option.direction[0])),
                    (-option.direction[1], option.direction[0]),
                    1,
                )
            )
            next_options.append(
                Option(
                    add(option.pos, (option.direction[1], -option.direction[0])),
                    (option.direction[1], -option.direction[0]),
                    1,
                ),
            )

        for n in next_options:
            if n.pos not in grid:
                continue

            current_score = grid[n.pos] + score
            heapq.heappush(queue, (current_score, n))


def part1(inp: list[str]):
    grid = {}
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    start = (0, 0)
    end = (len(inp[0]) - 1, len(inp) - 1)
    return dijkstra(start, end, grid)


def part2(inp: list[str]):
    grid = {}
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    start = (0, 0)
    end = (len(inp[0]) - 1, len(inp) - 1)
    return dijkstra2(start, end, grid)


aoc = AoC(part_1=part1, part_2=part2)
inp = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
# aoc.assert_p1(inp, 102)
# aoc.submit_p1()

aoc.assert_p2(inp, 94)
aoc.assert_p2(
    """111111111111
999999999991
999999999991
999999999991
999999999991""",
    71,
)
aoc.submit_p2()
