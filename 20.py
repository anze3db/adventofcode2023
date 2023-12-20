from __future__ import annotations

from math import prod
from typing import Literal

from adventofcode import AoC

Pulse = Literal["high", "low"]


def from_line(
    line: str,
    name_to_node: dict[str, FlipFlop | Conjunction | Broadcaster],
    counter: dict[Pulse, int],
):
    node, destinations = line.split(" -> ")
    destinations = destinations.split(", ")
    if node.startswith("%"):
        node = FlipFlop(
            name=node[1:],
            destinations=destinations,
            name_to_node=name_to_node,
            counter=counter,
        )
    elif node.startswith("&"):
        node = Conjunction(
            name=node[1:],
            destinations=destinations,
            name_to_node=name_to_node,
            counter=counter,
        )
    else:
        node = Broadcaster(
            name=node,
            destinations=destinations,
            name_to_node=name_to_node,
            counter=counter,
        )
    name_to_node[node.name] = node
    return node


def set_conjunctions(name_to_node: dict[str, FlipFlop | Conjunction | Broadcaster]):
    to_add = []
    for node in name_to_node.values():
        for destination in node.destinations:
            if destination not in name_to_node:
                n = Broadcaster(
                    name=destination,
                    destinations=[],
                    name_to_node=name_to_node,
                    counter=node.counter,
                )
                to_add.append(n)
            else:
                n = name_to_node[destination]
            if isinstance(n, Conjunction):
                n.state[node.name] = "low"
    for node in to_add:
        name_to_node[node.name] = node


class FlipFlop:
    def __init__(
        self,
        name: str,
        destinations: list[str],
        name_to_node: dict[str, FlipFlop | Conjunction | Broadcaster],
        counter: dict[Pulse, int],
    ):
        self.name = name
        self.destinations = destinations
        self.name_to_node = name_to_node
        self.state = False
        self.counter = counter

    def __repr__(self):
        return f"<FlipFlop {self.name} {self.state}>"

    def pulse(
        self, pulse: Pulse, _: FlipFlop | Conjunction | Broadcaster
    ) -> Pulse | None:
        if self.name == "rx" and pulse == "low":
            raise
        self.counter[pulse] += 1
        if pulse == "high":
            return None
        self.state = not self.state
        if self.state:
            pulse = "high"
        else:
            pulse = "low"
        return pulse

    def propagate(self, pulse: Pulse):
        pulses = {}
        for destination in self.destinations:
            if pulse is not None:
                # print(f"{self.name} -{pulse}-> {destination}")
                pulses[destination] = self.name_to_node[destination].pulse(pulse, self)
        for destination in self.destinations:
            if pulse is not None:
                self.name_to_node[destination].propagate(pulses[destination])


class Conjunction:
    def __init__(
        self,
        name: str,
        destinations: list[str],
        name_to_node: dict[str, FlipFlop | Conjunction | Broadcaster],
        counter: dict[Pulse, int],
    ):
        self.name = name
        self.state = {}
        self.name_to_node = name_to_node
        self.destinations = destinations
        self.counter = counter
        self.sent_pulse: Pulse = "low"

    def __repr__(self):
        return f"<Conjunction {self.name} {set(self.state.values()) == {"high"}}>"

    def pulse(
        self, pulse: Pulse, source: FlipFlop | Conjunction | Broadcaster
    ) -> Pulse | None:
        if self.name == "rx" and pulse == "low":
            raise
        self.state[source.name] = pulse
        self.counter[pulse] += 1
        if set(self.state.values()) == {"high"}:
            pulse = "low"
        else:
            pulse = "high"
            self.sent_pulse = "high"
        return pulse

    def propagate(self, pulse: Pulse):
        pulses = {}
        for destination in self.destinations:
            if pulse is not None:
                # print(f"{self.name} -{pulse}-> {destination}")
                pulses[destination] = self.name_to_node[destination].pulse(pulse, self)
        for destination in self.destinations:
            if pulse is not None:
                self.name_to_node[destination].propagate(pulses[destination])


class Broadcaster:
    def __init__(
        self,
        name: str,
        destinations: list[str],
        name_to_node: dict[str, FlipFlop | Conjunction | Broadcaster],
        counter: dict[Pulse, int],
    ):
        self.name = name
        self.destinations = destinations
        self.name_to_node = name_to_node
        self.counter = counter

    def __repr__(self):
        return "<Broadcaster>"

    def pulse(
        self, pulse: Pulse, _: FlipFlop | Conjunction | Broadcaster
    ) -> Pulse | None:
        if self.name == "rx" and pulse == "low":
            raise
        self.counter[pulse] += 1
        pulses = {}
        for destination in self.destinations:
            if pulse is not None:
                # print(f"{self.name} -{pulse}-> {destination}")
                pulses[destination] = self.name_to_node[destination].pulse(pulse, self)
        for destination in self.destinations:
            if pulse is not None:
                self.name_to_node[destination].propagate(pulses[destination])

    def propagate(self, pulse: Pulse):
        pass


def part1(inp: list[str]):
    name_to_node = {}
    counter: dict[Pulse, int] = {
        "low": 0,
        "high": 0,
    }
    for line in inp:
        from_line(line, name_to_node, counter)
    set_conjunctions(name_to_node)

    for i in range(1000):
        name_to_node["broadcaster"].pulse("low", None)
    return counter["high"] * (counter["low"])


def part2(inp: list[str]):
    name_to_node = {}
    counter: dict[Pulse, int] = {
        "low": 0,
        "high": 0,
    }
    for line in inp:
        from_line(line, name_to_node, counter)
    set_conjunctions(name_to_node)

    cnt = 0
    cycles = {n.name: 0 for n in name_to_node.values() if "kl" in n.destinations}

    while 0 in cycles.values():
        cnt += 1
        name_to_node["broadcaster"].pulse("low", None)
        for node in cycles:
            if cycles[node] == 0 and name_to_node[node].sent_pulse == "high":
                cycles[node] = cnt

    return prod(cycles.values())


aoc = AoC(part_1=part1, part_2=part2)
inp = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
inp2 = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
aoc.assert_p1(inp, 32000000)
aoc.assert_p1(inp2, 11687500)
aoc.submit_p1()

aoc.submit_p2()
