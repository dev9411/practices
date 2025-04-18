import unittest
from rain_water_trap import RainWaterTrap

class TestRainWaterTrap(unittest.TestCase):
    def setUp(self):
        self.trap = RainWaterTrap()

    def test_without_enough_walls(self):
        self.assertEqual(self.trap.trap([]), 0)
        self.assertEqual(self.trap.trap([4]), 0)
        self.assertEqual(self.trap.trap([4,5]), 0)

    def test_with_predefined_walls(self):
        self.assertEqual(self.trap.trap([5,5,5]), 0)
        self.assertEqual(self.trap.trap([5, 0, 1]), 1)
        self.assertEqual(self.trap.trap([5, 0, 5]), 5)
        self.assertEqual(self.trap.trap([3, 0, 4]), 3)
        self.assertEqual(self.trap.trap([5, 5, 0, 5]), 5)
        self.assertEqual(self.trap.trap([9, 8, 7, 6, 5, 9]), 10)
        self.assertEqual(self.trap.trap([100, 0, 0, 0, 0, 100]), 400)
        
    def test_all_ascending(self):
        self.assertEqual(self.trap.trap([1, 2, 3, 4, 5]), 0)
        self.assertEqual(self.trap.trap([10, 24, 35, 46, 59]), 0)
        
    def test_all_descending(self):
        self.assertEqual(self.trap.trap([91, 82, 73, 64, 55]), 0)
        self.assertEqual(self.trap.trap([10, 9, 8, 7, 6, 1]), 0)
        
    def test_random_series(self):
        self.assertEqual(self.trap.trap([2, 1, 0, 1, 3]), 4)
        self.assertEqual(self.trap.trap([0, 1, 0, 2, 1, 0, 1]), 2)
        self.assertEqual(self.trap.trap([0, 1, 0, 2, 1, 0, 1, 3]), 5)
        self.assertEqual(self.trap.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(self.trap.trap([4, 2, 0, 3, 2, 5]), 9)

    def test_with_huge_input(self):
        self.assertEqual(self.trap.trap(list(range(20000, 0, -1))), 0)
