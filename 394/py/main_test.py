import unittest

from main import Solution


class TestDecodeString(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self) -> None:
        self.assertEqual(self.sol.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_example_2_nested(self) -> None:
        self.assertEqual(self.sol.decodeString("3[a2[c]]"), "accaccacc")

    def test_example_3(self) -> None:
        self.assertEqual(self.sol.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_no_encoding(self) -> None:
        self.assertEqual(self.sol.decodeString("abc"), "abc")

    def test_empty(self) -> None:
        self.assertEqual(self.sol.decodeString(""), "")

    def test_multi_digit_count(self) -> None:
        self.assertEqual(self.sol.decodeString("10[a]"), "a" * 10)

    def test_deeply_nested(self) -> None:
        self.assertEqual(self.sol.decodeString("2[2[2[a]]]"), "a" * 8)

    def test_text_around(self) -> None:
        self.assertEqual(self.sol.decodeString("x2[y]z"), "xyyz")


if __name__ == "__main__":
    unittest.main()
