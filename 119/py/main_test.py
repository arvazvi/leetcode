import unittest

from main import Solution


class TestPascalTriangleII(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_row_0(self) -> None:
        self.assertEqual(self.sol.getRow(0), [1])

    def test_row_1(self) -> None:
        self.assertEqual(self.sol.getRow(1), [1, 1])

    def test_example_3(self) -> None:
        self.assertEqual(self.sol.getRow(3), [1, 3, 3, 1])

    def test_row_4(self) -> None:
        self.assertEqual(self.sol.getRow(4), [1, 4, 6, 4, 1])

    def test_row_5(self) -> None:
        # primer caso calculado a partir de la fila anterior
        self.assertEqual(self.sol.getRow(5), [1, 5, 10, 10, 5, 1])

    def test_row_6(self) -> None:
        self.assertEqual(self.sol.getRow(6), [1, 6, 15, 20, 15, 6, 1])

    def test_max_row(self) -> None:
        row = self.sol.getRow(33)
        self.assertEqual(len(row), 34)
        self.assertEqual(sum(row), 2**33)
        self.assertEqual(row[0], 1)
        self.assertEqual(row[-1], 1)
        self.assertEqual(row[1], 33)


if __name__ == "__main__":
    unittest.main()
