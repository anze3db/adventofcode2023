from functools import cache
from textwrap import dedent

import more_itertools
from adventofcode import AoC

aoc = AoC()


def part1(inp: list[str]):
    res = 0
    for line in inp:
        springs, counts = line.split(" ")
        counts = [int(c) for c in counts.split(",")]
        num_unknown = springs.count("?")
        num_set = springs.count("#")
        num_to_permutate = sum(counts) - num_set
        str_to_permutate = num_to_permutate * ["#"] + (
            (num_unknown - num_to_permutate) * ["."]
        )
        # Find all permutations of str_to_permutate
        all_permutations = more_itertools.distinct_permutations(str_to_permutate)
        # Replace ? with permutations
        for permutation in all_permutations:
            new_springs = springs
            for char in permutation:
                new_springs = new_springs.replace("?", char, 1)
            if [len(s) for s in new_springs.split(".") if s] == counts:
                res += 1

    return res


@cache
def dp(springs, counts, done_cnt=0):
    if not springs:
        if not counts and not done_cnt:
            return 1
        else:
            return 0

    sol_cnt = 0

    if springs[0] in ("#", "?"):
        sol_cnt += dp(springs[1:], counts, done_cnt + 1)
        # handle ending:
        if len(springs) == 1:
            if counts and done_cnt + 1 == counts[0]:
                sol_cnt += dp("", counts[1:], 0)
    if springs[0] in (".", "?"):
        if not done_cnt:
            sol_cnt += dp(springs[1:], counts, done_cnt)
        else:
            if counts and done_cnt == counts[0]:
                sol_cnt += dp(springs[1:], counts[1:], 0)
            else:
                # dead end, don't do anything
                pass

    return sol_cnt


def part2(inp: list[str]):
    res = 0
    for line in inp:
        springs, counts = line.split(" ")
        counts = [int(c) for c in counts.split(",")]
        res += dp("?".join(springs.split() * 5), tuple(counts * 5))
    return res


assert (
    part1(
        dedent(
            """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
        ).splitlines()
    )
    == 21
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
        ).splitlines()
    )
    == 525152
)
aoc.submit_p2(part2(aoc.get_input()))
