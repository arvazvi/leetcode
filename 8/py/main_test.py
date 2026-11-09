import unittest

from main import Solution


class TestMyAtoi(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self) -> None:
        self.assertEqual(self.sol.myAtoi("42"), 42)

    def test_example_2(self) -> None:
        self.assertEqual(self.sol.myAtoi(" -042"), -42)

    def test_example_3(self) -> None:
        self.assertEqual(self.sol.myAtoi("1337c0d3"), 1337)

    def test_example_4(self) -> None:
        self.assertEqual(self.sol.myAtoi("0-1"), 0)

    def test_example_5(self) -> None:
        self.assertEqual(self.sol.myAtoi("words and 987"), 0)

    def test_empty(self) -> None:
        self.assertEqual(self.sol.myAtoi(""), 0)

    def test_only_spaces(self) -> None:
        self.assertEqual(self.sol.myAtoi("    "), 0)

    def test_plus_sign(self) -> None:
        self.assertEqual(self.sol.myAtoi("+7"), 7)

    def test_sign_without_digits(self) -> None:
        self.assertEqual(self.sol.myAtoi("-"), 0)

    def test_double_sign(self) -> None:
        self.assertEqual(self.sol.myAtoi("+-12"), 0)

    def test_overflow_positive(self) -> None:
        self.assertEqual(self.sol.myAtoi("2147483648"), 2**31 - 1)

    def test_overflow_negative(self) -> None:
        self.assertEqual(self.sol.myAtoi("-91283472332"), -(2**31))

    def test_bounds(self) -> None:
        self.assertEqual(self.sol.myAtoi("2147483647"), 2**31 - 1)
        self.assertEqual(self.sol.myAtoi("-2147483648"), -(2**31))


if __name__ == "__main__":
    unittest.main()
