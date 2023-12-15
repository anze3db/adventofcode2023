import re
from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


def part1(inp: list[str]):
    res = 0
    for line in inp:
        digits = re.sub("[^0-9]", "", line)
        res += int(digits[0] + digits[-1])
    return res


def first_digit(line: str) -> str:
    if line[0].isdigit():
        return line[0]
    if line.startswith("one"):
        return "1"
    if line.startswith("two"):
        return "2"
    if line.startswith("three"):
        return "3"
    if line.startswith("four"):
        return "4"
    if line.startswith("five"):
        return "5"
    if line.startswith("six"):
        return "6"
    if line.startswith("seven"):
        return "7"
    if line.startswith("eight"):
        return "8"
    if line.startswith("nine"):
        return "9"
    return first_digit(line[1:])


def last_digit(line: str) -> str:
    if line[-1].isdigit():
        return line[-1]
    if line.endswith("one"):
        return "1"
    if line.endswith("two"):
        return "2"
    if line.endswith("three"):
        return "3"
    if line.endswith("four"):
        return "4"
    if line.endswith("five"):
        return "5"
    if line.endswith("six"):
        return "6"
    if line.endswith("seven"):
        return "7"
    if line.endswith("eight"):
        return "8"
    if line.endswith("nine"):
        return "9"
    return last_digit(line[:-1])


def part2(inp: list[str]):
    res = 0
    for line in inp:
        res += int(first_digit(line) + last_digit(line))
    return res


assert (
    part1(
        dedent(
            """1abc2
               pqr3stu8vwx
               a1b2c3d4e5f
               treb7uchet"""
        ).splitlines()
    )
    == 142
)
aoc.submit_p1(part1(aoc.get_input()))
assert (
    part2(
        dedent(
            """two1nine
            eightwothree
            abcone2threexyz 
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen"""
        ).splitlines()
    )
    == 281
)
aoc.submit_p2(part2(aoc.get_input()))
