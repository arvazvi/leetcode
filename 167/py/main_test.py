import unittest

from main import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_leetcode_example_1(self) -> None:
        # numbers = [2,7,11,15], target = 9 -> [1,2]
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_leetcode_example_2(self) -> None:
        # numbers = [2,3,4], target = 6 -> [1,3]
        self.assertEqual(self.sol.twoSum([2, 3, 4], 6), [1, 3])

    def test_leetcode_example_3(self) -> None:
        # numbers = [-1,0], target = -1 -> [1,2]
        self.assertEqual(self.sol.twoSum([-1, 0], -1), [1, 2])

    def test_min_length(self) -> None:
        # dos elementos que suman el target
        self.assertEqual(self.sol.twoSum([1, 2], 3), [1, 2])

    def test_first_and_last(self) -> None:
        # la solucion esta en los extremos
        self.assertEqual(self.sol.twoSum([1, 2, 3, 4, 5], 6), [1, 5])

    def test_adjacent_middle(self) -> None:
        # la solucion esta en el medio: 3 + 9 = 12
        self.assertEqual(self.sol.twoSum([1, 3, 5, 7, 9], 12), [2, 5])

    def test_negative_numbers(self) -> None:
        # [-5,-3,-1,2], target=-4 — -3+(-1)=-4 -> [2,3]
        self.assertEqual(self.sol.twoSum([-5, -3, -1, 2], -4), [2, 3])

    def test_all_negative(self) -> None:
        self.assertEqual(self.sol.twoSum([-10, -5, -3, -1], -8), [2, 3])

    def test_zeros_in_array(self) -> None:
        self.assertEqual(self.sol.twoSum([0, 0, 1, 2], 0), [1, 2])

    def test_target_zero_with_negatives(self) -> None:
        self.assertEqual(self.sol.twoSum([-3, -1, 1, 4], 0), [2, 3])

    def test_large_values(self) -> None:
        self.assertEqual(self.sol.twoSum([1000, 2000, 3000, 4000], 5000), [1, 4])

    def test_two_first_equal(self) -> None:
        # [1,1,2,3], target=2 — dos elementos iguales que suman
        self.assertEqual(self.sol.twoSum([1, 1, 2, 3], 2), [1, 2])

    def test_duplicate_values(self) -> None:
        # [1,2,3,3,4], target=6 — 2+4=6 -> [2,5]
        self.assertEqual(self.sol.twoSum([1, 2, 3, 3, 4], 6), [2, 5])

    def test_returns_1_indexed(self) -> None:
        # verificar que los indices son 1-based, no 0-based
        result = self.sol.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(min(result), 1)
        self.assertTrue(all(i > 0 for i in result))

    def test_returns_list_of_two(self) -> None:
        result = self.sol.twoSum([2, 3, 4], 6)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

    def test_big_sorted_array(self) -> None:
        # array grande ordenado
        numbers = list(range(1, 101))
        self.assertEqual(self.sol.twoSum(numbers, 199), [99, 100])

    def test_sparse_target(self) -> None:
        # [1,2,3,...,100], target=50 — 1+49=50 -> [1,49]
        self.assertEqual(self.sol.twoSum(list(range(1, 101)), 50), [1, 49])

    def test_singleton_at_start(self) -> None:
        # la solucion es el primer par
        self.assertEqual(self.sol.twoSum([1, 4, 5, 6], 5), [1, 2])


if __name__ == "__main__":
    unittest.main()
