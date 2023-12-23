import functools
import sys
from collections import deque

from adventofcode import AoC

print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)


def print_grid(grid: dict[tuple[int, int], str], start, end, visited=set()):
    min_x = min(x for x, _ in grid.keys())
    max_x = max(x for x, _ in grid.keys())
    min_y = min(y for _, y in grid.keys())
    max_y = max(y for _, y in grid.keys())
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == start:
                print("S", end="")
            elif (x, y) == end:
                print("E", end="")

            elif (x, y) in visited:
                print("o", end="")
            else:
                print(grid[(x, y)], end="")
        print()


def dfs(grid: dict[tuple[int, int], str], start, end, visited=None) -> int:
    if visited is None:
        visited = set()

    if start in visited:
        return 0

    if start == end:
        # print_grid(grid, start, end, visited)
        return len(visited)

    match grid.get(start):
        case "#" | None:
            return 0
        case ".":
            visited.add(start)
            return max(
                dfs(grid, (start[0] + 1, start[1]), end, visited.copy()),
                dfs(grid, (start[0] - 1, start[1]), end, visited.copy()),
                dfs(grid, (start[0], start[1] + 1), end, visited.copy()),
                dfs(grid, (start[0], start[1] - 1), end, visited.copy()),
            )
        case "v":
            visited.add(start)
            return dfs(grid, (start[0], start[1] + 1), end, visited.copy())
        case "^":
            visited.add(start)
            return dfs(grid, (start[0], start[1] - 1), end, visited.copy())
        case ">":
            visited.add(start)
            return dfs(grid, (start[0] + 1, start[1]), end, visited.copy())
        case "<":
            visited.add(start)
            return dfs(grid, (start[0] - 1, start[1]), end, visited.copy())


@functools.lru_cache(maxsize=None)
def skip_path_edge(start, end) -> tuple[int, int] | None:
    v = set([start])
    while True:
        if start == end:
            return start
        possible_next = tuple(
            p
            for p in (
                (start[0] - 1, start[1]),
                (start[0] + 1, start[1]),
                (start[0], start[1] - 1),
                (start[0], start[1] + 1),
            )
            if p not in v and grid.get(p) in (".", "v", "^", ">", "<")
        )

        if len(possible_next) == 0:
            return start
        elif len(possible_next) == 1:
            start = possible_next[0]
            v.add(start)
        else:
            return start


grid = {}


def dfs2(
    grid: dict[tuple[int, int], str], start, end, visited: set[tuple[int, int]]
) -> int:
    global current_max

    visited.add(start)
    # Optimization since most of the time there is only one possible next:

    next_start = skip_path_edge(start, end)
    if not next_start:
        return 0

    if next_start == end:
        if len(visited) > current_max:
            current_max = len(visited)
            print(current_max)
        return len(visited) - 1
    possible_next = tuple(
        p
        for p in (
            (start[0] + 1, start[1]),
            (start[0] - 1, start[1]),
            (start[0], start[1] + 1),
            (start[0], start[1] - 1),
        )
        if p not in visited and grid.get(p) in (".", "v", "^", ">", "<")
    )
    if not possible_next:
        return 0
    return max([dfs2(grid, p, end, visited.copy()) for p in possible_next])


def part1(inp: list[str]):
    grid = {}
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            grid[(i, j)] = c
    start = (1, 0)
    end = (len(inp[0]) - 2, len(inp) - 1)
    return dfs(grid, start, end)


def bfs(grid: dict[tuple[int, int], str], start, end) -> int:
    visited = set()
    queue = deque([(start, set([start]))])
    max_steps = 0
    while queue:
        start, visited = queue.pop()
        start = skip_path_edge(start, end)
        if start is None:
            continue

        possible_next = tuple(
            p
            for p in (
                (start[0] + 1, start[1]),
                (start[0], start[1] - 1),
                (start[0] - 1, start[1]),
                (start[0], start[1] + 1),
            )
            if p not in visited and grid.get(p) in (".", "v", "^", ">", "<")
        )
        if len(possible_next) == 1:
            start = possible_next[0]
            visited.add(start)
        for x, y in possible_next:
            if (x, y) == end:
                if max_steps < len(visited):
                    print(len(visited))
                    max_steps = len(visited)
            else:
                queue.append(((x, y), visited | set([(x, y)])))
    return max_steps


current_max = 0


def part2(inp: list[str]):
    grid = {}
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            grid[(i, j)] = c
    start = (1, 0)
    end = (len(inp[0]) - 2, len(inp) - 1)
    return bfs(grid, start, end)
    return dfs2(grid, start, end, visited=set())


aoc = AoC(part_1=part1, part_2=part2)
inp = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
aoc.assert_p1(inp, 94)
aoc.submit_p1()

aoc.assert_p2(inp, 154)
aoc.submit_p2()
