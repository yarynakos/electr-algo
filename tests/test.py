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
