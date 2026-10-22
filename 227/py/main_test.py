import unittest

from main import Solution


class TestBasicCalculatorII(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Solution()

    def test_addition(self) -> None:
        self.assertEqual(self.calc.calculate("1 + 1"), 2)

    def test_subtraction(self) -> None:
        self.assertEqual(self.calc.calculate(" 2-1 + 2 "), 3)

    def test_multiplication(self) -> None:
        self.assertEqual(self.calc.calculate("3+2*2"), 7)

    def test_division_truncate(self) -> None:
        self.assertEqual(self.calc.calculate(" 3/2 "), 1)

    def test_division_negative_truncate(self) -> None:
        self.assertEqual(self.calc.calculate("0-3/2"), -1)

    def test_mixed_precedence(self) -> None:
        self.assertEqual(self.calc.calculate(" 3+5 / 2 "), 5)

    def test_single_number(self) -> None:
        self.assertEqual(self.calc.calculate("42"), 42)

    def test_spaces(self) -> None:
        self.assertEqual(self.calc.calculate("   42   "), 42)

    def test_multidigit(self) -> None:
        self.assertEqual(self.calc.calculate("123 + 456"), 579)

    def test_subtraction_chain(self) -> None:
        self.assertEqual(self.calc.calculate("10 - 5 - 3"), 2)

    def test_all_ops(self) -> None:
        self.assertEqual(self.calc.calculate("1+2*5/3+6/4/2"), 4)

    def test_large(self) -> None:
        self.assertEqual(self.calc.calculate("14-3/2"), 13)

    def test_div_by_one(self) -> None:
        self.assertEqual(self.calc.calculate("100/1/2"), 50)

    def test_zero_result(self) -> None:
        self.assertEqual(self.calc.calculate("5-5"), 0)

    def test_multiplication_before_addition(self) -> None:
        self.assertEqual(self.calc.calculate("2*3+4"), 10)

    def test_division_before_subtraction(self) -> None:
        self.assertEqual(self.calc.calculate("10-6/2"), 7)

    def test_all_multiplication(self) -> None:
        self.assertEqual(self.calc.calculate("2*3*4"), 24)

    def test_all_division(self) -> None:
        self.assertEqual(self.calc.calculate("100/2/5"), 10)


if __name__ == "__main__":
    unittest.main()
