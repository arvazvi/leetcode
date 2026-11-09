import unittest

from main import Solution


class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring(""), 0)

    def test_single_char(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("a"), 1)

    def test_all_unique(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("abcdef"), 6)

    def test_with_spaces_and_symbols(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("a b!c a"), 5)

    def test_repeat_at_window_start(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("abba"), 2)

    def test_dvdf(self) -> None:
        self.assertEqual(self.sol.lengthOfLongestSubstring("dvdf"), 3)


if __name__ == "__main__":
    unittest.main()
