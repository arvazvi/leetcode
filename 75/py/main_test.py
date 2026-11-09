import unittest

from main import Solution


class TestSortColors(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def sort(self, colors: list[int]) -> list[int]:
        self.sol.sortColors(colors)
        return colors

    def test_example_1(self) -> None:
        self.assertEqual(self.sort([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])

    def test_example_2(self) -> None:
        self.assertEqual(self.sort([2, 0, 1]), [0, 1, 2])

    def test_single(self) -> None:
        self.assertEqual(self.sort([1]), [1])

    def test_already_sorted(self) -> None:
        self.assertEqual(self.sort([0, 1, 2]), [0, 1, 2])

    def test_reversed(self) -> None:
        self.assertEqual(self.sort([2, 2, 1, 1, 0, 0]), [0, 0, 1, 1, 2, 2])

    def test_all_same(self) -> None:
        self.assertEqual(self.sort([1, 1, 1]), [1, 1, 1])

    def test_two_colors(self) -> None:
        self.assertEqual(self.sort([2, 0, 2, 0]), [0, 0, 2, 2])


if __name__ == "__main__":
    unittest.main()
