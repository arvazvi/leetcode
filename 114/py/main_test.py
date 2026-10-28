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


def flatten_to_list(root: TreeNode | None) -> list[int]:
    """Recorre la lista enlazada resultante (solo punteros right) y devuelve los vals."""
    out: list[int] = []
    cur = root
    while cur:
        out.append(cur.val)
        # despues de flatten, left debe ser None
        assert cur.left is None, f"left no es None en nodo {cur.val}"
        cur = cur.right
    return out


class TestFlatten(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.sol.flatten(None)

    def test_single_node(self) -> None:
        root = TreeNode(1)
        self.sol.flatten(root)
        self.assertEqual(flatten_to_list(root), [1])

    def test_example_1(self) -> None:
        #        1
        #       / \
        #      2   5
        #     / \   \
        #    3   4   6
        #  -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        root = build_tree([1, 2, 5, 3, 4, None, 6])
        self.sol.flatten(root)
        self.assertEqual(flatten_to_list(root), [1, 2, 3, 4, 5, 6])

    def test_left_skewed(self) -> None:
        # 1 -> 2 -> 3  (todo a la izquierda)
        #     1
        #    /
        #   2
        #  /
        # 3
        root = build_tree([1, 2, None, 3])
        self.sol.flatten(root)
        self.assertEqual(flatten_to_list(root), [1, 2, 3])

    def test_right_skewed(self) -> None:
        #     1
        #      \
        #       2
        #        \
        #         3
        root = build_tree([1, None, 2, None, 3])
        self.sol.flatten(root)
        self.assertEqual(flatten_to_list(root), [1, 2, 3])

    def test_full_tree(self) -> None:
        #        1
        #       / \
        #      2   3
        #     / \ / \
        #    4  5 6  7
        #  -> 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.sol.flatten(root)
        self.assertEqual(flatten_to_list(root), [1, 2, 4, 5, 3, 6, 7])

    def test_two_levels(self) -> None:
        #     1
        #    / \
        #   2   3
        root = build_tree([1, 2, 3])
        self.sol.flatten(root)
        self.assertEqual(flatten_to_list(root), [1, 2, 3])

    def test_deep_left(self) -> None:
        #       1
        #      /
        #     2
        #    /
        #   3
        #  /
        # 4
        root = build_tree([1, 2, None, 3, None, 4])
        self.sol.flatten(root)
        self.assertEqual(flatten_to_list(root), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
