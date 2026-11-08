import unittest

from main import Solution


class TestMergeAlternately(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_same_length(self) -> None:
        self.assertEqual(self.sol.mergeAlternately("abc", "pqr"), "apbqcr")

    def test_word2_longer(self) -> None:
        self.assertEqual(self.sol.mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_word1_longer(self) -> None:
        self.assertEqual(self.sol.mergeAlternately("abcd", "pq"), "apbqcd")

    def test_single_chars(self) -> None:
        self.assertEqual(self.sol.mergeAlternately("a", "b"), "ab")

    def test_word1_empty(self) -> None:
        self.assertEqual(self.sol.mergeAlternately("", "xyz"), "xyz")

    def test_word2_empty(self) -> None:
        self.assertEqual(self.sol.mergeAlternately("xyz", ""), "xyz")

    def test_both_empty(self) -> None:
        self.assertEqual(self.sol.mergeAlternately("", ""), "")


if __name__ == "__main__":
    unittest.main()
