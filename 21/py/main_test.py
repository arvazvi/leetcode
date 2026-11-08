import unittest

from main import ListNode, Solution


def build_list(values: list[int]) -> ListNode | None:
    head: ListNode | None = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: ListNode | None) -> list[int]:
    out: list[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def merge(self, a: list[int], b: list[int]) -> list[int]:
        return to_list(self.sol.mergeTwoLists(build_list(a), build_list(b)))

    def test_both_empty(self) -> None:
        self.assertIsNone(self.sol.mergeTwoLists(None, None))

    def test_first_empty(self) -> None:
        self.assertEqual(self.merge([], [0]), [0])

    def test_second_empty(self) -> None:
        self.assertEqual(self.merge([1, 2], []), [1, 2])

    def test_example_1(self) -> None:
        self.assertEqual(self.merge([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])

    def test_no_overlap(self) -> None:
        self.assertEqual(self.merge([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_no_overlap_reversed(self) -> None:
        self.assertEqual(self.merge([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])

    def test_different_lengths(self) -> None:
        self.assertEqual(self.merge([1], [0, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_equal_values(self) -> None:
        self.assertEqual(self.merge([2, 2], [2, 2]), [2, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
