import math
import queue
from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


class Map:
    def __init__(self, config):
        self.name = config[0].split(" ")[0]
        self.destination_ranges = []
        self.source_ranges = []
        for line in config[1:]:
            destination, source, amount = map(int, line.split(" "))
            self.destination_ranges.append((destination, destination + amount))
            self.source_ranges.append((source, source + amount))

    def __getitem__(self, key):
        for i, (start, end) in enumerate(self.source_ranges):
            if start <= key <= end:
                return self.destination_ranges[i][0] + (key - start)
        return key


def parse_maps(maps):
    for m in maps.split("\n\n"):
        yield Map(m.split("\n"))


def parse_maps2(maps):
    for m in maps.split("\n\n"):
        yield Map2(m.split("\n"))


def part1(inp):
    seeds = map(int, inp[0].split(": ")[1].split(" "))
    maps_to_parse = "\n".join(inp[2:])
    maps = list(parse_maps(maps_to_parse))

    locations = []
    for seed in seeds:
        next_to_parse = seed
        for m in maps:
            next_to_parse = m[next_to_parse]
        locations.append(next_to_parse)
    return min(locations)


def lazy_ranges(seed_ranges):
    seed_ranges = list(seed_ranges)
    for i in range(0, len(seed_ranges), 2):
        yield [
            (seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]),
        ]


class Map2(Map):
    def __getitem__(self, key_ranges):
        new_ranges = set()
        to_check = set(key_ranges)

        while to_check:
            key_start, key_end = to_check.pop()
            hit = False
            for i, (start, end) in enumerate(self.source_ranges):
                dest_start, _ = self.destination_ranges[i]
                diff = dest_start - start
                if start <= key_start <= key_end <= end:
                    new_ranges.add(
                        (
                            key_start + diff,
                            key_end + diff,
                        )
                    )
                    hit = True
                elif key_start < start <= key_end <= end:
                    new_ranges.add((key_start, start - 1))
                    to_check.add((key_start, start - 1))
                    new_ranges.add(
                        (
                            start + diff,
                            key_end + diff,
                        )
                    )
                    hit = True
                elif start <= key_start <= end < key_end:
                    new_ranges.add(
                        (
                            key_start + diff,
                            end + diff,
                        )
                    )
                    to_check.add((end + 1, key_end))
                    new_ranges.add((end + 1, key_end))
                    hit = True
                elif key_start < start <= end < key_end:
                    new_ranges.add((key_start, start - 1))
                    to_check.add((key_start, start - 1))
                    new_ranges.add(
                        (
                            start + diff,
                            end + diff,
                        )
                    )
                    new_ranges.add((end + 1, key_end))
                    to_check.add((end + 1, key_end))
                    hit = True

            if not hit:
                new_ranges.add((key_start, key_end))
        return new_ranges


def part2(inp):
    seed_ranges = map(int, inp[0].split(": ")[1].split(" "))

    maps_to_parse = "\n".join(inp[2:])
    maps = list(parse_maps2(maps_to_parse))

    min_location = math.inf
    for seed in lazy_ranges(seed_ranges):
        next_to_parse = seed
        for m in maps:
            next_to_parse = m[next_to_parse]
        min_from_ranges = min(
            [min(n[0], n[1]) for n in next_to_parse], default=math.inf
        )
        if min_from_ranges < min_location:
            min_location = min_from_ranges

    return min_location


assert (
    part1(
        dedent(
            """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
        ).splitlines()
    )
    == 35
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
        ).splitlines()
    )
    == 46
)
aoc.submit_p2(part2(aoc.get_input()))
