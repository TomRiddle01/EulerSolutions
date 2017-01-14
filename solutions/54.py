from Euler import *
import unittest

ranks = ["1","2","3","4","5","6","7","8","9","T","J","Q","K","A"]
ranks_indicies = list(range(15))
hand_ranks = []


royal_flush = set([13,12,11,10,9])

straight_flushes = [set(ranks_indicies[i:(i+5)]) for i in range(11)]


def handType(hand):
    suits = [x[1] for x in hand]
    suits_set = set(suits)
    hand = [ranks.index(x[0]) for x in hand]
    hand_set = set(hand)

    # royal flush
    if hand_set == royal_flush and len(suits_set) == 1: return (10, highest(hand_set))

    # straight flush
    if len(suits_set) == 1:
        for flush in straight_flushes:
            if hand_set == flush: return (9, highest(flush))

    # 4 of a kind
    of_a_kind = 0
    for c in hand:
        count = hand.count(c)
        if count == 4:
            of_a_kind = 4
            of_a_kind_card = c
            break
        if count == 3:
            of_a_kind = 3
            of_a_kind_card = c
            break

    if of_a_kind == 4: return (8, c)

    # full house
    if of_a_kind == 3 and len(hand_set) == 2: return (7, highest(hand_set))

    # flush
    if len(suits_set) == 1: return (6, highest(hand_set))

    # straight flush
    for flush in straight_flushes:
        if hand_set == flush: return (5, highest(flush))

    # three of a kind
    if of_a_kind == 3: return (4, c)

    # two pairs
    if len(hand_set) == 3: return (3, highest(c for c in hand_set if hand.count(c) == 2))

    # one pair
    if len(hand_set) == 4: return (2, highest(c for c in hand_set if hand.count(c) == 2))

    return (1, highest(hand))


def highest(hand):
    hand = list(hand)
    hand.sort()
    hand.reverse()
    return tuple(hand)

def wins(player, enemy):
    t1 = handType(player)
    t2 = handType(enemy)
    return t1 > t2


class TestHands(unittest.TestCase):

    def setUp(self):
        pass

    def test_full_house(self):
        self.assertEqual(handType("TC JC QC KC AC".split(" ")[0]), 10)
        self.assertEqual(handType("TH JH QH KH AH".split(" ")[0]), 10)
        self.assertNotEqual(handType("TH JH QH KH AC".split(" ")[0]), 10)

    def test_straight_flush(self):
        self.assertEqual(handType("1C 2C 3C 4C 5C".split(" "))[0], 9)
        self.assertEqual(handType("6H 7H 8H 9H TH".split(" "))[0], 9)
        self.assertNotEqual(handType("TH JH QH KH AC".split(" "))[0], 9)
        self.assertNotEqual(handType("1H 2H 3H 4H 6H".split(" "))[0], 9)

    def test_four_of_a_kind(self):
        self.assertEqual(handType("1C 1C 1C 1H 5C".split(" "))[0], 8)
        self.assertEqual(handType("9H 7H 9H 9H 9H".split(" "))[0], 8)
        self.assertNotEqual(handType("2H 2H 2H KH AC".split(" "))[0], 8)
        self.assertNotEqual(handType("1H 2H 2H 2H 6H".split(" "))[0], 8)

    def test_full_house(self):
        self.assertEqual(handType("1C 1C 1C 2H 2C".split(" "))[0], 7)
        self.assertEqual(handType("9H 7H 7H 7H 9H".split(" "))[0], 7)
        self.assertNotEqual(handType("2H 2H 2H 2H AC".split(" "))[0], 7)
        self.assertNotEqual(handType("2H 2H 2H 2H 6H".split(" "))[0], 7)

    def test_flush(self):
        self.assertEqual(handType("1C 1C 3C 2C 2C".split(" "))[0], 6)
        self.assertEqual(handType("9H 7H 4H 7H 9H".split(" "))[0], 6)
        self.assertNotEqual(handType("2H 2C 2H 2H AC".split(" "))[0], 6)
        self.assertNotEqual(handType("2H 2C 2H 2H 6H".split(" "))[0], 6)

    def test_straight(self):
        self.assertEqual(handType("1C 2H 3C 4C 5C".split(" "))[0], 5)
        self.assertEqual(handType("5H 6C 7H 8C 9H".split(" "))[0], 5)
        self.assertNotEqual(handType("1C 2C 3C 4C 5C".split(" "))[0], 5)
        self.assertNotEqual(handType("2H 2C 2H 2H 6H".split(" "))[0], 5)

    def test_three_of_a_kind(self):
        self.assertEqual(handType("1C 1H 1C 4C 5C".split(" "))[0], 4)
        self.assertEqual(handType("5H 3C 3H 3C 9H".split(" "))[0], 4)
        self.assertNotEqual(handType("3C 3C 3C 3C 5C".split(" "))[0], 4)
        self.assertNotEqual(handType("2H 2C 2H 2H 6H".split(" "))[0], 4)

    def test_two_pairs(self):
        self.assertEqual(handType("1C 1H 2C 2C 5C".split(" "))[0], 3)
        self.assertEqual(handType("3H 3C 2H 2C 9H".split(" "))[0], 3)
        self.assertNotEqual(handType("3C 3C 3C 3C 2C".split(" "))[0], 3)
        self.assertNotEqual(handType("2H 2C 2H 2H 2H".split(" "))[0], 3)

    def test_two_pairs(self):
        self.assertEqual(handType("1C 1H 2C 2C 5C".split(" "))[0], 3)
        self.assertEqual(handType("3H 3C 2H 2C 9H".split(" "))[0], 3)
        self.assertNotEqual(handType("3C 3C 3C 3C 2C".split(" "))[0], 3)
        self.assertNotEqual(handType("2H 2C 2H 2H 2H".split(" "))[0], 3)

    def test_one_pair(self):
        self.assertEqual(handType("1C 1H 2C 7C 5C".split(" "))[0], 2)
        self.assertEqual(handType("3H 7C 2H 2C 9H".split(" "))[0], 2)
        self.assertNotEqual(handType("3C 3C 3C 3C 2C".split(" "))[0], 2)
        self.assertNotEqual(handType("2H 2C 2H 2H 2H".split(" "))[0], 2)

    def test_highest_value(self):
        self.assertEqual(handType("1C 4H 2C 7C 5C".split(" "))[0], 1)
        self.assertEqual(handType("3H 7C 4H 2C 9H".split(" "))[0], 1)
        self.assertEqual(handType("2H 2C 2H 2H 2H".split(" "))[0], 1) # assumption
        self.assertNotEqual(handType("3C 3C 3C 3C 2C".split(" "))[0], 1)

#unittest.main(); exit()


matchups = []
with open("solutions/54_poker.txt") as file:
    for line in file.readlines():
        match = line.strip().split(" ")
        matchups.append((match[:5], match[5:]))

w = 0
for player1, player2 in matchups:
    
    if wins(player1,player2):
        w += 1
verify(w)



