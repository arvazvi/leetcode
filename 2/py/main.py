class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

def sum_lists(l1: ListNode | None, l2: ListNode | None, carry: int = 0) -> ListNode | None:
    if not l1 and not l2 and carry == 0:
        return None

    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0

    total = v1 + v2 + carry
    new_carry = total // 10
    digit = total % 10

    result = ListNode(digit)
    next_l1 = l1.next if l1 else None
    next_l2 = l2.next if l2 else None

    result.next = sum_lists(next_l1, next_l2, new_carry)
    return result
