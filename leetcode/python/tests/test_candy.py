import unittest
from candy import CandySolution

class TestCandySolution(unittest.TestCase):
    def setUp(self):
        self.solution = CandySolution()

    def test_single_child(self):
        self.assertEqual(self.solution.candy([5]), 1)

    def test_equal_ratings(self):
        self.assertEqual(self.solution.candy([1, 1, 1, 1]), 4)

    def test_increasing_ratings(self):
        self.assertEqual(self.solution.candy([1, 2, 3, 4, 5]), 15)

    def test_decreasing_ratings(self):
        self.assertEqual(self.solution.candy([5, 4, 3, 2, 1]), 15)

    def test_peak_and_valley(self):
        self.assertEqual(self.solution.candy([1, 2, 3, 2, 1]), 9)

    def test_random_case(self):
        self.assertEqual(self.solution.candy([1, 0, 2]), 5)
        self.assertEqual(self.solution.candy([1, 2, 2]), 4)

    def test_another_random_case(self):
        self.assertEqual(self.solution.candy([1, 3, 2, 2, 1]), 7)

if __name__ == '__main__':
    unittest.main()
