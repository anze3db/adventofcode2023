from adventofcode import AoC


def hsh(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def part1(inp):
    p = sum([hsh(s) for s in inp.strip().split(",")])
    return p


def part2(inp):
    steps = inp.strip().split(",")
    hashmap = {i: [] for i in range(256)}
    for step in steps:
        if "-" in step:
            k = hsh(step[:-1])
            hashmap[k] = [lense for lense in hashmap[k] if lense[0] != step[:-1]]
        else:
            label, value = step.split("=")
            k = hsh(label)
            for i, lense in enumerate(hashmap[k]):
                if lense[0] == label:
                    hashmap[k][i] = label, value
                    break
            else:
                hashmap[k].append((label, value))
    res = 0
    for i in range(256):
        for j, lense in enumerate(hashmap[i]):
            res += (i + 1) * (j + 1) * int(lense[1])
    return res


aoc = AoC(part_1=part1, part_2=part2, auto_splitlines=False)
aoc.test_p1("""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7\n""", 1320)
aoc.submit_p1()

aoc.test_p2("""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7\n""", 145)
aoc.submit_p2()
