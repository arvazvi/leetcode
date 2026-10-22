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


class TestIsSymmetric(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.assertTrue(self.sol.isSymmetric(None))

    def test_single(self) -> None:
        root = TreeNode(1)
        self.assertTrue(self.sol.isSymmetric(root))

    def test_leetcode_example_1(self) -> None:
        # [1,2,2,3,4,4,3] — simetrico
        root = build_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_leetcode_example_2(self) -> None:
        # [1,2,2,None,3,None,3] — no simetrico
        root = build_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_two_levels_symmetric(self) -> None:
        root = build_tree([1, 2, 2])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_two_levels_asymmetric_values(self) -> None:
        # [1,2,3] — valores distintos en los hijos
        root = build_tree([1, 2, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_left_skewed(self) -> None:
        # [1,2,None,3] — solo hijo izquierdo
        root = build_tree([1, 2, None, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_right_skewed(self) -> None:
        # [1,None,2,None,3] — solo hijo derecho
        root = build_tree([1, None, 2, None, 3])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_full_three_levels_symmetric(self) -> None:
        # arbol perfecto de 4 niveles: [1,2,2,3,4,4,3,5,6,6,5,5,6,6,5]
        root = build_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, 6, 5, 5, 6, 6, 5])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_deep_mirrored(self) -> None:
        # [1,2,2,3,None,None,3] — espejo perfecto de 3 niveles
        root = build_tree([1, 2, 2, 3, None, None, 3])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_deep_mismatch_inner(self) -> None:
        # [1,2,2,3,None,3,None] — desbalance interior
        root = build_tree([1, 2, 2, 3, None, 3, None])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_large_symmetric(self) -> None:
        # arbol perfecto de 5 niveles (1..31) — no es simetrico por valores,
        # pero construimos uno simetrico a mano.
        # Nivel 0: 1
        # Nivel 1: 2, 2
        # Nivel 2: 3,4 / 4,3
        # Nivel 3: 5,6,7,8 / 8,7,6,5
        values: list[int | None] = [1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5]
        root = build_tree(values)
        self.assertTrue(self.sol.isSymmetric(root))

    def test_negative_values_symmetric(self) -> None:
        root = build_tree([-1, -2, -2, -3, -4, -4, -3])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_negative_values_asymmetric(self) -> None:
        root = build_tree([-1, -2, -2, -3, -4, -4, 4])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_two_node_symmetric_same_value(self) -> None:
        # [1,2,2] con mismo valor
        root = build_tree([1, 2, 2])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_two_node_asymmetric_structure(self) -> None:
        # [1,2] — solo un hijo
        root = build_tree([1, 2])
        self.assertFalse(self.sol.isSymmetric(root))

    def test_values_zero(self) -> None:
        # [0,0,0] — todos cero, simetrico
        root = build_tree([0, 0, 0])
        self.assertTrue(self.sol.isSymmetric(root))

    def test_one_child_none_other_not(self) -> None:
        # [1,2,2,None,3,None,None] — estructura asimetrica
        root = build_tree([1, 2, 2, None, 3, None, None])
        self.assertFalse(self.sol.isSymmetric(root))


if __name__ == "__main__":
    unittest.main()
