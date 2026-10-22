import unittest

from main import Solution


def evaluate(expression: str) -> int:
    return Solution().calculate(expression)


class TestBasicCalculator(unittest.TestCase):
    def test_simple_addition(self) -> None:
        self.assertEqual(evaluate("1 + 1"), 2)

    def test_simple_subtraction(self) -> None:
        self.assertEqual(evaluate(" 2-1 + 2 "), 3)

    def test_nested_parens(self) -> None:
        self.assertEqual(evaluate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_single_number(self) -> None:
        self.assertEqual(evaluate("1"), 1)

    def test_zero(self) -> None:
        self.assertEqual(evaluate("0"), 0)

    def test_spaces(self) -> None:
        self.assertEqual(evaluate("   42   "), 42)

    def test_multidigit(self) -> None:
        self.assertEqual(evaluate("123 + 456"), 579)

    def test_only_parens(self) -> None:
        self.assertEqual(evaluate("(((42)))"), 42)

    def test_unary_minus_leading(self) -> None:
        self.assertEqual(evaluate("-2 + 3"), 1)

    def test_unary_minus_in_parens(self) -> None:
        self.assertEqual(evaluate("1-(-2)"), 3)

    def test_double_negation(self) -> None:
        self.assertEqual(evaluate("-(-5)"), 5)

    def test_subtraction_chain(self) -> None:
        self.assertEqual(evaluate("10 - 5 - 3"), 2)

    def test_all_ops(self) -> None:
        self.assertEqual(evaluate("1 + 2 - 3 + 4 - 5"), -1)

    def test_complex(self) -> None:
        self.assertEqual(evaluate("((10 - 5) + (2 + 3))"), 10)

    def test_leading_unary_in_parens(self) -> None:
        self.assertEqual(evaluate("-(2+3)"), -5)

    def test_unary_after_open_paren(self) -> None:
        self.assertEqual(evaluate("2+(-3)"), -1)

    def test_double_unary_in_parens(self) -> None:
        self.assertEqual(evaluate("2-(-(-3))"), -1)

    def test_large_expression(self) -> None:
        self.assertEqual(evaluate("(1+(4+5+2)-3)+(6+8)"), 23)


if __name__ == "__main__":
    unittest.main()
