class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val: int = val
        self.next: ListNode | None = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        decoy = ListNode(0, head)

        prev = decoy
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                if prev:
                    prev.next = head.next
            else:
                if prev:
                    prev = prev.next
            head = head.next
        return decoy.next