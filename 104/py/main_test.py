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


class TestMaxDepth(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.assertEqual(self.sol.maxDepth(None), 0)

    def test_single(self) -> None:
        root = TreeNode(1)
        self.assertEqual(self.sol.maxDepth(root), 1)

    def test_leetcode_example_1(self) -> None:
        # [3,9,20,None,None,15,7] -> 3
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.sol.maxDepth(root), 3)

    def test_leetcode_example_2(self) -> None:
        # [1,None,2] -> 2
        root = build_tree([1, None, 2])
        self.assertEqual(self.sol.maxDepth(root), 2)

    def test_two_levels_full(self) -> None:
        # [1,2,3] -> 2
        root = build_tree([1, 2, 3])
        self.assertEqual(self.sol.maxDepth(root), 2)

    def test_left_skewed(self) -> None:
        # [1,2,None,3,None,4] -> 4
        root = build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.sol.maxDepth(root), 4)

    def test_right_skewed(self) -> None:
        # [1,None,2,None,3,None,4] -> 4
        root = build_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.sol.maxDepth(root), 4)

    def test_perfect_three_levels(self) -> None:
        # [1,2,3,4,5,6,7] -> 3
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.maxDepth(root), 3)

    def test_perfect_four_levels(self) -> None:
        # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] -> 4
        root = build_tree(list(range(1, 16)))
        self.assertEqual(self.sol.maxDepth(root), 4)

    def test_perfect_five_levels(self) -> None:
        # 1..31 -> 5
        root = build_tree(list(range(1, 32)))
        self.assertEqual(self.sol.maxDepth(root), 5)

    def test_negative_values(self) -> None:
        root = build_tree([-1, -2, -3, -4, -5])
        self.assertEqual(self.sol.maxDepth(root), 3)

    def test_zero_values(self) -> None:
        root = build_tree([0, 0, 0])
        self.assertEqual(self.sol.maxDepth(root), 2)

    def test_unbalanced_left(self) -> None:
        # [1,2,3,4,None,None,None,5] -> 4
        root = build_tree([1, 2, 3, 4, None, None, None, 5])
        self.assertEqual(self.sol.maxDepth(root), 4)

    def test_unbalanced_right(self) -> None:
        # [1,None,2,None,3,None,4,None,5] -> 5
        root = build_tree([1, None, 2, None, 3, None, 4, None, 5])
        self.assertEqual(self.sol.maxDepth(root), 5)

    def test_one_child_only(self) -> None:
        # [1,2] -> 2
        root = build_tree([1, 2])
        self.assertEqual(self.sol.maxDepth(root), 2)

    def test_deep_with_gaps(self) -> None:
        # [1,None,2,3,None,4,5,None,None,6] -> 5
        # nivel 0: 1
        # nivel 1: 2 (hijo derecho)
        # nivel 2: 3 (hijo izquierdo de 2)
        # nivel 3: 4,5 (hijos de 3)
        # nivel 4: 6 (hijo de 4)
        root = build_tree([1, None, 2, 3, None, 4, 5, None, None, 6])
        self.assertEqual(self.sol.maxDepth(root), 5)

    def test_large_perfect(self) -> None:
        # arbol perfecto de 10 niveles: 1..1023 -> 10
        values: list[int | None] = list(range(1, 1024))
        root = build_tree(values)
        self.assertEqual(self.sol.maxDepth(root), 10)


if __name__ == "__main__":
    unittest.main()
