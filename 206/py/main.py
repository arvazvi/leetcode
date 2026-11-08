class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val: int = val
        self.next: ListNode | None = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        p, c = None, head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
