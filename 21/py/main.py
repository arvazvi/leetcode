class ListNode:
    def __init__(self, val: int = 0, nxt: ListNode | None = None) -> None:
        self.val: int = val
        self.next: ListNode | None = nxt

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
