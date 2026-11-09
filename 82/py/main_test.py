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


class TestDeleteDuplicates(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def run_case(self, values: list[int]) -> list[int]:
        return to_list(self.sol.deleteDuplicates(build_list(values)))

    def test_example_1(self) -> None:
        self.assertEqual(self.run_case([1, 2, 3, 3, 4, 4, 5]), [1, 2, 5])

    def test_example_2(self) -> None:
        self.assertEqual(self.run_case([1, 1, 1, 2, 3]), [2, 3])

    def test_empty(self) -> None:
        self.assertIsNone(self.sol.deleteDuplicates(None))

    def test_single(self) -> None:
        self.assertEqual(self.run_case([1]), [1])

    def test_all_duplicates(self) -> None:
        self.assertEqual(self.run_case([2, 2, 2]), [])

    def test_no_duplicates(self) -> None:
        self.assertEqual(self.run_case([1, 2, 3]), [1, 2, 3])

    def test_duplicates_at_end(self) -> None:
        self.assertEqual(self.run_case([1, 2, 3, 3]), [1, 2])

    def test_consecutive_duplicate_groups(self) -> None:
        self.assertEqual(self.run_case([1, 1, 2, 2, 3]), [3])


if __name__ == "__main__":
    unittest.main()
