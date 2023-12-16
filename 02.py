import math

from adventofcode import AoC


def part1(input):
    ids = set()
    impossible = set()
    for line in input:
        id_, games = line.split(": ")
        id_ = int(id_.split(" ")[1])
        ids.add(id_)
        games = games.split("; ")
        possible = {
            "blue": 14,
            "green": 13,
            "red": 12,
        }
        for game in games:
            game = game.split(", ")
            for cube in game:
                num, color = cube.split(" ")
                if int(num) > possible[color]:
                    impossible.add(id_)
    return sum(ids - impossible)


def part2(input):
    res = 0
    for line in input:
        _, games = line.split(": ")
        games = games.split("; ")
        possible = {
            "blue": 0,
            "green": 0,
            "red": 0,
        }
        for game in games:
            game = game.split(", ")
            for cube in game:
                num, color = cube.split(" ")
                if int(num) > possible[color]:
                    possible[color] = int(num)
        res += math.prod(possible.values())

    return res


aoc = AoC(part_1=part1, part_2=part2)

inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
aoc.assert_p1(
    inp,
    8,
)
aoc.submit_p1()

aoc.assert_p2(
    inp,
    2286,
)
aoc.submit_p2()
