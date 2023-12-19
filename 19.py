import math

from adventofcode import AoC


def parse_workflow_rule(rule):
    if "<" in rule:
        return rule.split("<")[0], "__lt__", int(rule.split("<")[1])
    elif ">" in rule:
        return rule.split(">")[0], "__gt__", int(rule.split(">")[1])


def parse_workflow(workflow_list):
    return [
        (w.split(":")[1], parse_workflow_rule(w.split(":")[0]))
        for w in workflow_list[:-1]
    ] + [(workflow_list[-1], None)]


def parse_part_list(part_list):
    return {p.split("=")[0]: int(p.split("=")[1]) for p in part_list}


def part1(inp: str):
    workflows, parts = inp.split("\n\n")
    workflows = workflows.splitlines()
    parts = parts.splitlines()

    initial_workflow = "in"
    workflows = {
        w.split("{")[0]: parse_workflow(w.split("{")[1].split("}")[0].split(","))
        for w in workflows
    }
    parts = [
        parse_part_list(p.replace("{", "").replace("}", "").split(",")) for p in parts
    ]
    res = 0
    for part in parts:
        workflow = initial_workflow
        while workflow not in ("A", "R"):
            for step, rule in workflows[workflow]:
                if rule is None:
                    workflow = step
                    break
                elif getattr(part[rule[0]], rule[1])(rule[2]):
                    workflow = step
                    break
        if workflow == "A":
            res += sum(part.values())
    return res


class Part2:
    def __init__(self, workflows):
        self.workflows = workflows
        self.count = 0

    def all_cnt(self, lows, highs):
        return math.prod(
            max(high - low, 0) for (low, high) in zip(lows.values(), highs.values())
        )

    def calc(self, workflow, lows, highs):
        if workflow == "A":
            self.count += self.all_cnt(lows, highs)
            return
        if workflow == "R":
            return

        for step, rule in self.workflows[workflow]:
            if rule is None:
                self.calc(step, lows, highs)
                continue

            part, op, val = rule

            if op == "__lt__":
                h = highs.copy()
                l = lows.copy()
                h[part] = min(h[part], val)
                if self.all_cnt(l, h) > 0:
                    self.calc(step, l, h)
                lows[part] = max(lows[part], val)
            elif op == "__gt__":
                h = highs.copy()
                l = lows.copy()
                l[part] = max(l[part], val + 1)
                if self.all_cnt(l, h) > 0:
                    self.calc(step, l, h)
                highs[part] = min(highs[part], val + 1)


def part2(inp: str):
    workflows, parts = inp.split("\n\n")
    workflows = workflows.splitlines()
    workflows = {
        w.split("{")[0]: parse_workflow(w.split("{")[1].split("}")[0].split(","))
        for w in workflows
    }
    lows = {"x": 1, "m": 1, "a": 1, "s": 1}
    highs = {"x": 4001, "m": 4001, "a": 4001, "s": 4001}
    inital_workflow = "in"
    workflows = Part2(workflows)
    workflows.calc(inital_workflow, lows, highs)
    return workflows.count


aoc = AoC(part_1_no_splitlines=part1, part_2_no_splitlines=part2)
inp = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
aoc.assert_p1(inp, 19114)
aoc.submit_p1()

aoc.assert_p2(inp, 167409079868000)
aoc.submit_p2()
