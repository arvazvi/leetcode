import unittest

from main import Solution


class TestWordSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        self.board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]

    def test_example_1(self) -> None:
        self.assertTrue(self.sol.exist(self.board, "ABCCED"))

    def test_example_2(self) -> None:
        self.assertTrue(self.sol.exist(self.board, "SEE"))

    def test_example_3_reuse_cell(self) -> None:
        self.assertFalse(self.sol.exist(self.board, "ABCB"))

    def test_single_cell_match(self) -> None:
        self.assertTrue(self.sol.exist([["a"]], "a"))

    def test_single_cell_no_match(self) -> None:
        self.assertFalse(self.sol.exist([["a"]], "b"))

    def test_single_cell_reuse(self) -> None:
        self.assertFalse(self.sol.exist([["a"]], "aa"))

    def test_single_row_reversed(self) -> None:
        self.assertTrue(self.sol.exist([["a", "b"]], "ba"))

    def test_word_longer_than_board(self) -> None:
        self.assertFalse(self.sol.exist([["a", "b"]], "abab"))

    def test_backtracking_needed(self) -> None:
        # el primer camino posible desde (0,0) falla; hay que retroceder
        board = [["a", "a"], ["a", "b"]]
        self.assertTrue(self.sol.exist(board, "aaab"))

    def test_not_diagonal(self) -> None:
        board = [["a", "b"], ["c", "d"]]
        self.assertFalse(self.sol.exist(board, "ad"))


if __name__ == "__main__":
    unittest.main()
