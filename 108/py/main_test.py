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


def in_order(root: TreeNode | None) -> list[int]:
    """Recorrido in-order del arbol."""
    if root is None:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)


def height(root: TreeNode | None) -> int:
    """Altura del arbol (numero de aristas hasta la hoja mas profunda)."""
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root: TreeNode | None) -> bool:
    """True si en cada nodo la diferencia de alturas entre hijos es <= 1."""
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    return abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right)


class TestSortedArrayToBST(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.assertIsNone(self.sol.sortedArrayToBST([]))

    def test_single(self) -> None:
        root = self.sol.sortedArrayToBST([0])
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 0)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_two_elements(self) -> None:
        root = self.sol.sortedArrayToBST([-10, -3])
        self.assertIn(root.val, [-10, -3])
        self.assertEqual(in_order(root), [-10, -3])
        self.assertTrue(is_balanced(root))

    def test_example_1(self) -> None:
        nums = [-10, -3, 0, 5, 9]
        root = self.sol.sortedArrayToBST(nums)
        # in-order de un BST construido de un array ordenado debe ser el array.
        self.assertEqual(in_order(root), nums)
        self.assertTrue(is_balanced(root))

    def test_example_2(self) -> None:
        nums = [1, 3]
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(in_order(root), nums)
        self.assertTrue(is_balanced(root))

    def test_odd_length(self) -> None:
        nums = list(range(-5, 6))  # 11 elementos
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(in_order(root), nums)
        self.assertTrue(is_balanced(root))

    def test_even_length(self) -> None:
        nums = list(range(-4, 5))  # 9 elementos
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(in_order(root), nums)
        self.assertTrue(is_balanced(root))

    def test_negative_only(self) -> None:
        nums = [-5, -4, -3, -2, -1]
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(in_order(root), nums)
        self.assertTrue(is_balanced(root))

    def test_root_is_median_odd(self) -> None:
        # Con longitud impar la raiz es el elemento central exacto.
        nums = [1, 2, 3, 4, 5]
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(root.val, 3)

    def test_large_balanced(self) -> None:
        nums = list(range(1, 32))  # 31 elementos -> arbol perfecto de altura 4
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(in_order(root), nums)
        self.assertTrue(is_balanced(root))


if __name__ == "__main__":
    unittest.main()
