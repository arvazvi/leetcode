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


class TestReverseList(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_empty(self) -> None:
        self.assertIsNone(self.sol.reverseList(None))

    def test_single_node(self) -> None:
        self.assertEqual(to_list(self.sol.reverseList(build_list([1]))), [1])

    def test_two_nodes(self) -> None:
        self.assertEqual(to_list(self.sol.reverseList(build_list([1, 2]))), [2, 1])

    def test_example_1(self) -> None:
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(self.sol.reverseList(head)), [5, 4, 3, 2, 1])

    def test_duplicates(self) -> None:
        head = build_list([1, 1, 2, 2])
        self.assertEqual(to_list(self.sol.reverseList(head)), [2, 2, 1, 1])


if __name__ == "__main__":
    unittest.main()
