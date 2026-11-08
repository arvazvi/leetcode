import unittest

from main import Solution


class TestPascalTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_one_row(self) -> None:
        self.assertEqual(self.sol.generate(1), [[1]])

    def test_two_rows(self) -> None:
        self.assertEqual(self.sol.generate(2), [[1], [1, 1]])

    def test_example_5(self) -> None:
        self.assertEqual(
            self.sol.generate(5),
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        )

    def test_six_rows(self) -> None:
        # primer caso que sale del base precalculado
        res = self.sol.generate(6)
        self.assertEqual(len(res), 6)
        self.assertEqual(res[-1], [1, 5, 10, 10, 5, 1])

    def test_seven_rows(self) -> None:
        res = self.sol.generate(7)
        self.assertEqual(res[-1], [1, 6, 15, 20, 15, 6, 1])

    def test_max_rows(self) -> None:
        res = self.sol.generate(30)
        self.assertEqual(len(res), 30)
        for i, row in enumerate(res):
            self.assertEqual(len(row), i + 1)
            self.assertEqual(sum(row), 2**i)
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)


if __name__ == "__main__":
    unittest.main()
