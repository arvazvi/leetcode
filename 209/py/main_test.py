import unittest

from main import minSubArrayLen


class TestMinSubArrayLen(unittest.TestCase):
    def test_example_1(self) -> None:
        # target=7, nums=[2,3,1,2,4,3] -> subarreglo [4,3] de longitud 2
        self.assertEqual(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_example_2(self) -> None:
        # target=4, nums=[1,4,4] -> [4] de longitud 1
        self.assertEqual(minSubArrayLen(4, [1, 4, 4]), 1)

    def test_example_3(self) -> None:
        # target=11, nums=[1]*8 -> suma total 8 < 11 -> 0
        self.assertEqual(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)

    def test_empty(self) -> None:
        self.assertEqual(minSubArrayLen(5, []), 0)

    def test_single_element_ge_target(self) -> None:
        self.assertEqual(minSubArrayLen(5, [5]), 1)

    def test_single_element_lt_target(self) -> None:
        self.assertEqual(minSubArrayLen(10, [5]), 0)

    def test_whole_array_needed(self) -> None:
        # suma justo igual al target -> necesita todo el arreglo
        self.assertEqual(minSubArrayLen(15, [1, 2, 3, 4, 5]), 5)

    def test_whole_array_exact(self) -> None:
        self.assertEqual(minSubArrayLen(6, [1, 2, 3]), 3)

    def test_prefix(self) -> None:
        # [2,3] suma 5 >= 5 al inicio, luego se reduce a [3] que es < 5
        self.assertEqual(minSubArrayLen(5, [2, 3, 1, 1, 1, 1]), 2)

    def test_suffix(self) -> None:
        # el minimo subarreglo esta al final: [1,1,1,1,1,5] con target 5 -> [5]
        self.assertEqual(minSubArrayLen(5, [1, 1, 1, 1, 1, 5]), 1)

    def test_all_zeros(self) -> None:
        self.assertEqual(minSubArrayLen(1, [0, 0, 0, 0]), 0)

    def test_large_target_unreachable(self) -> None:
        self.assertEqual(minSubArrayLen(100, [1, 2, 3]), 0)

    def test_two_elements_exact(self) -> None:
        self.assertEqual(minSubArrayLen(3, [1, 2]), 2)

    def test_shrink_then_grow(self) -> None:
        # ventana: [2,3,1,2] suma 8 >= 7, contrae a [3,1,2] suma 6 < 7,
        # luego [3,1,2,4] suma 10, contrae a [4,3] suma 7 -> longitud 2
        self.assertEqual(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)


if __name__ == "__main__":
    unittest.main()
