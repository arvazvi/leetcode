import unittest

from main import Solution


class TestTrailingZeroes(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(3), 0)

    def test_example_2(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(5), 1)

    def test_zero(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(0), 0)

    def test_just_below_five(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(4), 0)

    def test_ten(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(10), 2)

    def test_twenty_five(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(25), 6)

    def test_hundred(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(100), 24)

    def test_upper_bound(self) -> None:
        self.assertEqual(self.sol.trailingZeroes(10000), 2499)


if __name__ == "__main__":
    unittest.main()
