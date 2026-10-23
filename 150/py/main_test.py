import unittest

from main import Solution


class TestEvalRPN(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_leetcode_example_1(self) -> None:
        # ["2","1","+","3","*"] -> (2+1)*3 = 9
        self.assertEqual(self.sol.evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test_leetcode_example_2(self) -> None:
        # ["4","13","5","/","+"] -> 4 + (13/5) = 4 + 2 = 6
        self.assertEqual(self.sol.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_leetcode_example_3(self) -> None:
        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # = 10 * (6 / ((9+3) * -11)) + 17 + 5 = 10 * (6 / -132) + 22 = 10 * 0 + 22 = 22
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(self.sol.evalRPN(tokens), 22)

    def test_single_number(self) -> None:
        self.assertEqual(self.sol.evalRPN(["42"]), 42)

    def test_single_negative_number(self) -> None:
        self.assertEqual(self.sol.evalRPN(["-7"]), -7)

    def test_single_zero(self) -> None:
        self.assertEqual(self.sol.evalRPN(["0"]), 0)

    def test_addition(self) -> None:
        self.assertEqual(self.sol.evalRPN(["3", "4", "+"]), 7)

    def test_subtraction(self) -> None:
        self.assertEqual(self.sol.evalRPN(["10", "3", "-"]), 7)

    def test_subtraction_negative_result(self) -> None:
        self.assertEqual(self.sol.evalRPN(["3", "10", "-"]), -7)

    def test_multiplication(self) -> None:
        self.assertEqual(self.sol.evalRPN(["6", "7", "*"]), 42)

    def test_multiplication_negative(self) -> None:
        self.assertEqual(self.sol.evalRPN(["-3", "5", "*"]), -15)

    def test_multiplication_two_negatives(self) -> None:
        self.assertEqual(self.sol.evalRPN(["-3", "-5", "*"]), 15)

    def test_division(self) -> None:
        self.assertEqual(self.sol.evalRPN(["13", "5", "/"]), 2)

    def test_division_exact(self) -> None:
        self.assertEqual(self.sol.evalRPN(["12", "4", "/"]), 3)

    def test_division_truncates_toward_zero(self) -> None:
        # 7 / -2 = -3.5 -> -3 (truncation toward zero)
        self.assertEqual(self.sol.evalRPN(["7", "-2", "/"]), -3)

    def test_division_negative_dividend(self) -> None:
        # -7 / 2 = -3.5 -> -3 (truncation toward zero)
        self.assertEqual(self.sol.evalRPN(["-7", "2", "/"]), -3)

    def test_division_by_one(self) -> None:
        self.assertEqual(self.sol.evalRPN(["100", "1", "/"]), 100)

    def test_division_result_zero(self) -> None:
        # 1 / 2 = 0.5 -> 0
        self.assertEqual(self.sol.evalRPN(["1", "2", "/"]), 0)

    def test_zero_numerator(self) -> None:
        self.assertEqual(self.sol.evalRPN(["0", "5", "/"]), 0)

    def test_chained_addition(self) -> None:
        # 1 2 + 3 + 4 + = 10
        self.assertEqual(self.sol.evalRPN(["1", "2", "+", "3", "+", "4", "+"]), 10)

    def test_chained_multiplication(self) -> None:
        # 2 3 * 4 * = 24
        self.assertEqual(self.sol.evalRPN(["2", "3", "*", "4", "*"]), 24)

    def test_mixed_operations(self) -> None:
        # 5 1 2 + 4 * + 3 - = 5 + (1+2)*4 - 3 = 5 + 12 - 3 = 14
        self.assertEqual(self.sol.evalRPN(["5", "1", "2", "+", "4", "*", "+", "3", "-"]), 14)

    def test_nested_expression(self) -> None:
        # (2+3) * (4-1) = 5 * 3 = 15
        # 2 3 + 4 1 - *
        self.assertEqual(self.sol.evalRPN(["2", "3", "+", "4", "1", "-", "*"]), 15)

    def test_large_numbers(self) -> None:
        self.assertEqual(self.sol.evalRPN(["1000", "2000", "+"]), 3000)

    def test_large_multiplication(self) -> None:
        self.assertEqual(self.sol.evalRPN(["1000", "1000", "*"]), 1000000)

    def test_negative_in_expression(self) -> None:
        # 3 -4 * = -12
        self.assertEqual(self.sol.evalRPN(["3", "-4", "*"]), -12)

    def test_complex_with_negatives(self) -> None:
        # -4 -3 + -> -7
        self.assertEqual(self.sol.evalRPN(["-4", "-3", "+"]), -7)

    def test_division_large(self) -> None:
        # 1000000 / 3 = 333333
        self.assertEqual(self.sol.evalRPN(["1000000", "3", "/"]), 333333)

    def test_all_operators(self) -> None:
        # 3 4 + 2 * 10 5 / -
        # = (3+4)*2 - (10/5) = 14 - 2 = 12
        self.assertEqual(self.sol.evalRPN(["3", "4", "+", "2", "*", "10", "5", "/", "-"]), 12)


if __name__ == "__main__":
    unittest.main()
