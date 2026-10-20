import unittest

from main import Solution, TreeNode


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Construye un arbol binario a partir de una lista por niveles (LeetCode)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
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


class TestLevelOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.assertEqual(self.sol.levelOrder(None), [])

    def test_single(self) -> None:
        root = TreeNode(1)
        self.assertEqual(self.sol.levelOrder(root), [[1]])

    def test_leetcode_example_1(self) -> None:
        # [3,9,20,None,None,15,7]
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.sol.levelOrder(root), [[3], [9, 20], [15, 7]])

    def test_leetcode_example_2(self) -> None:
        root = build_tree([1])
        self.assertEqual(self.sol.levelOrder(root), [[1]])

    def test_leetcode_example_3(self) -> None:
        # entrada vacia
        self.assertEqual(self.sol.levelOrder(build_tree([])), [])

    def test_left_skewed(self) -> None:
        # [1,2,None,3,None,4]
        root = build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.sol.levelOrder(root), [[1], [2], [3], [4]])

    def test_right_skewed(self) -> None:
        # [1,None,2,None,3]
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.sol.levelOrder(root), [[1], [2], [3]])

    def test_two_levels_full(self) -> None:
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.levelOrder(root), [[1], [2, 3], [4, 5, 6, 7]])

    def test_negative_values(self) -> None:
        root = build_tree([-1, -2, -3, -4, -5])
        self.assertEqual(self.sol.levelOrder(root), [[-1], [-2, -3], [-4, -5]])

    def test_deep_balanced(self) -> None:
        # arbol perfecto de 3 niveles: 1,2,3,4,5,6,7
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(
            self.sol.levelOrder(root),
            [[1], [2, 3], [4, 5, 6, 7]],
        )

    def test_large_balanced(self) -> None:
        # arbol perfecto de 5 niveles (1..31)
        values = list(range(1, 32))
        root = build_tree(values)
        expected = [
            [1],
            [2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        ]
        self.assertEqual(self.sol.levelOrder(root), expected)

    def test_interleaved_nones(self) -> None:
        # [1, None, 2, None, 3, None, 4]
        root = build_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.sol.levelOrder(root), [[1], [2], [3], [4]])

    def test_returns_lists_not_linked(self) -> None:
        # Los subniveles deben ser listas independientes: mutar una no afecta otra.
        root = build_tree([1, 2, 3])
        result = self.sol.levelOrder(root)
        result[0].append(99)
        self.assertEqual(self.sol.levelOrder(root), [[1], [2, 3]])


if __name__ == "__main__":
    unittest.main()
