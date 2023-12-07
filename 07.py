from functools import cmp_to_key
from textwrap import dedent

from adventofcode import AoC

aoc = AoC()


class Hand:
    ORDER = "AKQJT98765432"[::-1]

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid})"

    def compare(self, other):
        if self.type() > other.type():
            return 1
        elif self.type() < other.type():
            return -1
        else:
            for i in range(5):
                if self.ORDER.index(self.cards[i]) > self.ORDER.index(other.cards[i]):
                    return 1
                elif self.ORDER.index(self.cards[i]) < self.ORDER.index(other.cards[i]):
                    return -1

    def type(self):
        from collections import Counter

        counts = Counter(self.cards)
        if len(counts) == 5:
            return 1
        elif len(counts) == 4:
            return 2
        elif len(counts) == 3 and 3 not in counts.values():
            return 3
        elif len(counts) == 3 and 3 in counts.values():
            return 4
        elif len(counts) == 2 and 4 not in counts.values():
            return 5
        elif len(counts) == 2 and 4 in counts.values():
            return 6
        elif len(counts) == 1:
            return 7


class Hand2:
    ORDER = "AKQT98765432J"[::-1]

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid})"

    def compare(self, other):
        if self.type() > other.type():
            return 1
        elif self.type() < other.type():
            return -1
        else:
            for i in range(5):
                if self.ORDER.index(self.cards[i]) > self.ORDER.index(other.cards[i]):
                    return 1
                elif self.ORDER.index(self.cards[i]) < self.ORDER.index(other.cards[i]):
                    return -1

    def type(self):
        from collections import Counter

        mx = 0
        for c in self.ORDER:
            if "J" in self.cards:
                cards = self.cards.replace("J", c)
            else:
                cards = self.cards
            counts = Counter(cards)
            if len(counts) == 5:
                if mx < 1:
                    mx = 1
            elif len(counts) == 4:
                if mx < 2:
                    mx = 2
            elif len(counts) == 3 and 3 not in counts.values():
                if mx < 3:
                    mx = 3
            elif len(counts) == 3 and 3 in counts.values():
                if mx < 4:
                    mx = 4
            elif len(counts) == 2 and 4 not in counts.values():
                if mx < 5:
                    mx = 5
            elif len(counts) == 2 and 4 in counts.values():
                if mx < 6:
                    mx = 6
            elif len(counts) == 1:
                if mx < 7:
                    mx = 7
        return mx


def part1(inp):
    hands = []
    for line in inp:
        card, bid = line.split(" ")
        hand = Hand(card, int(bid))
        hands.append(hand)
    hands.sort(key=cmp_to_key(lambda item1, item2: item1.compare(item2)), reverse=False)
    res = 0
    for i, hand in enumerate(hands):
        res += hand.bid * (i + 1)
    return res


def part2(inp):
    hands = []
    for line in inp:
        card, bid = line.split(" ")
        hand = Hand2(card, int(bid))
        hands.append(hand)
    hands.sort(key=cmp_to_key(lambda item1, item2: item1.compare(item2)), reverse=False)
    res = 0
    for i, hand in enumerate(hands):
        res += hand.bid * (i + 1)
    return res


assert (
    part1(
        dedent(
            """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
        ).splitlines()
    )
    == 6440
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        dedent(
            """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
        ).splitlines()
    )
    == 5905
)
aoc.submit_p2(part2(aoc.get_input()))
