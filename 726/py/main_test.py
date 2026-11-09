import unittest

from main import Solution


class TestCountOfAtoms(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("H2O"), "H2O")

    def test_example_2(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("Mg(OH)2"), "H2MgO2")

    def test_example_3(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("K4(ON(SO3)2)2"), "K4N2O14S4")

    def test_concatenated(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("H2O2He3Mg4"), "H2He3Mg4O2")

    def test_single_atom(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("H"), "H")

    def test_group_without_count(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("(H2O2)"), "H2O2")

    def test_multi_digit_count(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("C12H22O11"), "C12H22O11")

    def test_nested_groups(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("((H)2O)3"), "H6O3")

    def test_repeated_atom_merges(self) -> None:
        self.assertEqual(self.sol.countOfAtoms("HOH"), "H2O")


if __name__ == "__main__":
    unittest.main()
