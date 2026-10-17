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


class TestRightSideView(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.assertEqual(self.sol.rightSideView(None), [])

    def test_single_node(self) -> None:
        self.assertEqual(self.sol.rightSideView(TreeNode(1)), [1])

    def test_example_1(self) -> None:
        #        1
        #       / \
        #      2   3
        #       \   \
        #        5   4
        root = build_tree([1, 2, 3, None, 5, None, 4])
        self.assertEqual(self.sol.rightSideView(root), [1, 3, 4])

    def test_example_2(self) -> None:
        root = build_tree([1, None, 3])
        self.assertEqual(self.sol.rightSideView(root), [1, 3])

    def test_left_skewed(self) -> None:
        # 1 -> 2 -> 3  (todo a la izquierda)
        root = build_tree([1, 2, None, 3])
        self.assertEqual(self.sol.rightSideView(root), [1, 2, 3])

    def test_right_skewed(self) -> None:
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.sol.rightSideView(root), [1, 2, 3])

    def test_full_tree(self) -> None:
        #        1
        #       / \
        #      2   3
        #     / \ / \
        #    4  5 6  7
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.rightSideView(root), [1, 3, 7])

    def test_rightmost_hidden(self) -> None:
        #        1
        #       / \
        #      2   3
        #     /   / \
        #    4   5   6
        #       /
        #      7
        root = build_tree([1, 2, 3, 4, None, 5, 6, None, None, 7])
        self.assertEqual(self.sol.rightSideView(root), [1, 3, 6, 7])


if __name__ == "__main__":
    unittest.main()
