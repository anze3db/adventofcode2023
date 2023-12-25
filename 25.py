import networkx as nx
from adventofcode import AoC


def part1(inp: list[str]):
    G = nx.Graph()
    for line in inp:
        a, b = line.split(": ")
        for link in b.split(" "):
            G.add_edge(a, link)
    comp = nx.community.girvan_newman(G)
    frst, scnd = tuple(sorted(c) for c in next(comp))
    print(frst, scnd)
    return len(frst) * len(scnd)


aoc = AoC(part_1=part1)
inp = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""
aoc.assert_p1(inp, 54)
aoc.submit_p1()
