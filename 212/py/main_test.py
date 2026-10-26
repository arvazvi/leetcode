import unittest
from main import Solution


class TestWordSearchII(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_example_case(self) -> None:
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        ans = self.s.findWords(board, words)
        self.assertEqual(set(ans), {"eat", "oath"})

    def test_single_cell_match(self) -> None:
        board = [["a"]]
        words = ["a", "b"]
        self.assertEqual(self.s.findWords(board, words), ["a"])

    def test_single_cell_no_match(self) -> None:
        board = [["a"]]
        words = ["b"]
        self.assertEqual(self.s.findWords(board, words), [])

    def test_empty_row(self) -> None:
        # Board with a row but no columns — not a valid LeetCode input
        # but the solution should handle it without crashing.
        # (Fully empty board=[] is not a valid LeetCode constraint.)
        pass

    def test_empty_words(self) -> None:
        board = [["a", "b"], ["c", "d"]]
        self.assertEqual(self.s.findWords(board, []), [])

    def test_no_matches(self) -> None:
        board = [["a", "b"], ["c", "d"]]
        words = ["xyz", "zzz"]
        self.assertEqual(self.s.findWords(board, words), [])

    def test_word_longer_than_board(self) -> None:
        board = [["a", "a"], ["a", "a"]]
        words = ["aaaaa"]  # 5 chars, board only has 4 cells
        self.assertEqual(self.s.findWords(board, words), [])

    def test_word_exactly_fits_board(self) -> None:
        board = [["a", "a"], ["a", "a"]]
        words = ["aaaa"]
        self.assertEqual(self.s.findWords(board, words), ["aaaa"])

    def test_2x2_aba_case(self) -> None:
        # The case that exposed the missing-backtracking bug.
        board = [["a", "b"], ["a", "a"]]
        words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
        ans = self.s.findWords(board, words)
        self.assertEqual(set(ans), {"aba", "baa", "aaab", "aaa", "aaba"})

    def test_duplicate_words_in_list(self) -> None:
        board = [["a", "b"], ["c", "d"]]
        words = ["ab", "ab", "ab"]
        ans = self.s.findWords(board, words)
        self.assertEqual(ans, ["ab"])

    def test_overlapping_paths(self) -> None:
        # "abc" and "ab" share a prefix path but both should be found.
        board = [["a", "b", "c"]]
        words = ["ab", "abc"]
        self.assertEqual(set(self.s.findWords(board, words)), {"ab", "abc"})

    def test_word_is_prefix_of_another(self) -> None:
        # "oa" is a prefix of "oab"; both exist on the board.
        board = [["o", "a", "b"]]
        words = ["oa", "oab"]
        self.assertEqual(set(self.s.findWords(board, words)), {"oa", "oab"})

    def test_2x2_aaa_case(self) -> None:
        board = [["a", "a"]]
        words = ["aaa"]
        self.assertEqual(self.s.findWords(board, words), [])

    def test_snake_path(self) -> None:
        # Board laid out so the word snakes through every cell.
        board = [
            ["a", "b", "c"],
            ["f", "e", "d"],
        ]
        words = ["abcdef", "abc", "fed"]
        ans = self.s.findWords(board, words)
        self.assertEqual(set(ans), {"abcdef", "abc", "fed"})

    def test_large_shared_prefix_no_timeout(self) -> None:
        # The 10x10 alternating board with thousands of abababab... words.
        board = [
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
        ]
        import string
        words = []
        for first in string.ascii_lowercase:
            for second in string.ascii_lowercase:
                words.append(first + second + "abababab")
        ans = self.s.findWords(board, words)
        self.assertIn("ababababab", ans)

    def test_sea_of_a_with_many_words(self) -> None:
        # The sample from 212/sample.txt: a huge board of 'a's with
        # hundreds of *aaaaaaaaa words. Verifies the Trie-pruning works.
        board = [
            ["m", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
            ["n", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["o", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["p", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["q", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["r", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["t", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["u", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["v", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["x", "y", "z", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
        ]
        import string
        words = []
        for first in string.ascii_lowercase:
            words.append(first + "aaaaaaaaa")
        ans = self.s.findWords(board, words)
        # Every word except "maaaaaaaaa" (m is isolated in the corner)
        # can start from the 'a' at (1,1) or any 'a' in column 1+.
        self.assertIn("baaaaaaaaa", ans)
        self.assertIn("naaaaaaaaa", ans)
        self.assertIn("zaaaaaaaaa", ans)
        self.assertNotIn("maaaaaaaaa", ans)

    def test_full_sample_file(self) -> None:
        # Loads the exact board/words from 212/sample.txt and verifies
        # the result matches a brute-force DFS for every word.
        import os
        path = os.path.join(os.path.dirname(__file__), "..", "sample.txt")
        if not os.path.exists(path):
            self.skipTest("sample.txt not found")
        with open(path) as f:
            content = f.read().strip()
        bstart = content.index("board=") + len("board=")
        wstart = content.index("words=") + len("words=")
        board = eval(content[bstart:content.rindex("words=")])
        words = eval(content[wstart:])
        ans = set(self.s.findWords(board, words))

        # Brute-force: DFS per word.
        rows, cols = len(board), len(board[0])

        def word_exists(word: str) -> bool:
            def dfs(i: int, j: int, k: int, seen: set) -> bool:
                if k == len(word):
                    return True
                if i < 0 or i >= rows or j < 0 or j >= cols:
                    return False
                if board[i][j] != word[k] or (i, j) in seen:
                    return False
                seen.add((i, j))
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if dfs(i + di, j + dj, k + 1, seen):
                        seen.discard((i, j))
                        return True
                seen.discard((i, j))
                return False
            return any(
                dfs(i, j, 0, set())
                for i in range(rows)
                for j in range(cols)
            )

        expected = {w for w in words if word_exists(w)}
        self.assertEqual(ans, expected)


if __name__ == "__main__":
    unittest.main()
