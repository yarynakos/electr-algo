import unittest

from src.main import find_the_longest_wire


class TestFindLongestWire(unittest.TestCase):

    def test_longest_wire(self):
        distance = 2
        pillar_list = [3, 3, 3]
        result = find_the_longest_wire(distance, pillar_list)
        self.assertAlmostEqual(result, 5.65, places=1)

    def test_short_wire(self):
        distance = 1
        pillar_list = [1, 1, 1]
        result = find_the_longest_wire(distance, pillar_list)
        self.assertAlmostEqual(result, 2.0)

    def test_empty_pillar_list(self):
        distance = 2
        pillar_list = []
        result = find_the_longest_wire(distance, pillar_list)
        self.assertEqual(result, 0)

    def test_short(self):
        distance = 4
        pillar_list = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95,
                       97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        result = find_the_longest_wire(distance, pillar_list)
        self.assertAlmostEqual(result, 2738.18, delta=0.01)
