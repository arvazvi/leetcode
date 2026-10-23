import unittest

from main import Solution, TreeNode


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Construye un arbol binario a partir de una lista por niveles (LeetCode)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue: list[TreeNode] = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestSumNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.assertEqual(self.sol.sumNumbers(None), 0)

    def test_single(self) -> None:
        root = TreeNode(5)
        self.assertEqual(self.sol.sumNumbers(root), 5)

    def test_leetcode_example_1(self) -> None:
        # [1,2,3] -> 12 + 13 = 25
        root = build_tree([1, 2, 3])
        self.assertEqual(self.sol.sumNumbers(root), 25)

    def test_leetcode_example_2(self) -> None:
        # [4,9,0,5,1] -> 495 + 491 + 40 = 1026
        root = build_tree([4, 9, 0, 5, 1])
        self.assertEqual(self.sol.sumNumbers(root), 1026)

    def test_left_skewed(self) -> None:
        # [1,2,None,3] -> 123
        root = build_tree([1, 2, None, 3])
        self.assertEqual(self.sol.sumNumbers(root), 123)

    def test_right_skewed(self) -> None:
        # [1,None,2,None,3] -> 123
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.sol.sumNumbers(root), 123)

    def test_deep_left(self) -> None:
        # [1,2,None,3,None,4] -> 1234
        root = build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.sol.sumNumbers(root), 1234)

    def test_three_levels_full(self) -> None:
        # [1,2,3,4,5,6,7] -> 124 + 125 + 136 + 137 = 522
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.sumNumbers(root), 522)

    def test_zero_root(self) -> None:
        # [0,1,2] -> 1 + 2 = 3
        root = build_tree([0, 1, 2])
        self.assertEqual(self.sol.sumNumbers(root), 3)

    def test_all_zeros(self) -> None:
        # [0,0,0] -> 0 + 0 = 0
        root = build_tree([0, 0, 0])
        self.assertEqual(self.sol.sumNumbers(root), 0)

    def test_one_child(self) -> None:
        # [1,2] -> 12
        root = build_tree([1, 2])
        self.assertEqual(self.sol.sumNumbers(root), 12)

    def test_one_child_right(self) -> None:
        # [1,None,2] -> 12
        root = build_tree([1, None, 2])
        self.assertEqual(self.sol.sumNumbers(root), 12)

    def test_unbalanced(self) -> None:
        # [1,2,3,4] -> 124 + 13 = 137
        root = build_tree([1, 2, 3, 4])
        self.assertEqual(self.sol.sumNumbers(root), 137)

    def test_negative_values(self) -> None:
        # [-1,-2,-3] -> -12 + -13 = -25
        root = build_tree([-1, -2, -3])
        self.assertEqual(self.sol.sumNumbers(root), -25)

    def test_large_single_chain(self) -> None:
        # [1,2,3,4,5] left-skewed -> 12345
        root = build_tree([1, 2, None, 3, None, 4, None, 5])
        self.assertEqual(self.sol.sumNumbers(root), 12345)

    def test_perfect_four_levels(self) -> None:
        # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        # paths: 1248+1249+1260+1261+1372+1373+1384+1385 = 10532
        values: list[int | None] = list(range(1, 16))
        root = build_tree(values)
        self.assertEqual(self.sol.sumNumbers(root), 10532)


if __name__ == "__main__":
    unittest.main()
