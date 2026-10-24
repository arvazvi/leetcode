import unittest

from main import ListNode, sum_lists


def build_list(digits: list[int]) -> ListNode | None:
    """Construye una lista enlazada a partir de una lista de digitos."""
    dummy = ListNode()
    cur = dummy
    for d in digits:
        cur.next = ListNode(d)
        cur = cur.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    """Convierte una lista enlazada de vuelta a una lista de digitos."""
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


class TestAddTwoNumbers(unittest.TestCase):
    def test_example1(self) -> None:
        # 342 + 465 = 807
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [7, 0, 8])

    def test_example2(self) -> None:
        # 0 + 0 = 0
        l1 = build_list([0])
        l2 = build_list([0])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [0])

    def test_example3(self) -> None:
        # 9999999 + 9999 = 10009998
        l1 = build_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_list([9, 9, 9, 9])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_different_lengths(self) -> None:
        # 99 + 1 = 100
        l1 = build_list([9, 9])
        l2 = build_list([1])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [0, 0, 1])

    def test_both_empty(self) -> None:
        result = sum_lists(None, None)
        self.assertIsNone(result)

    def test_one_empty(self) -> None:
        # 0 + 123 = 123
        l2 = build_list([3, 2, 1])
        result = sum_lists(None, l2)
        self.assertEqual(to_list(result), [3, 2, 1])

    def test_carry_single_digit(self) -> None:
        # 5 + 5 = 10
        l1 = build_list([5])
        l2 = build_list([5])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [0, 1])

    def test_nine_plus_nine(self) -> None:
        # 9 + 9 = 18
        l1 = build_list([9])
        l2 = build_list([9])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [8, 1])

    def test_all_nines(self) -> None:
        # 999 + 999 = 1998
        l1 = build_list([9, 9, 9])
        l2 = build_list([9, 9, 9])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [8, 9, 9, 1])

    def test_zeros_in_middle(self) -> None:
        # 101 + 202 = 303
        l1 = build_list([1, 0, 1])
        l2 = build_list([2, 0, 2])
        result = sum_lists(l1, l2)
        self.assertEqual(to_list(result), [3, 0, 3])


if __name__ == "__main__":
    unittest.main()
