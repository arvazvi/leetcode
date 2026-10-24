package main

type ListNode struct {
    Val int
    Next *ListNode
}

func sum(l1 *ListNode, l2 *ListNode, carry int) *ListNode {
    if l1 == nil && l2 == nil && carry == 0 {
        return nil
    }

    var v1, v2 int
    var nxt1, nxt2 *ListNode

    if l1 != nil {
        v1 = l1.Val
        nxt1 = l1.Next
    }
    if l2 != nil {
        v2 = l2.Val
        nxt2 = l2.Next
    }

    total := v1 + v2 + carry
    new_carry := total / 10
    digit := total % 10

    result := &ListNode{Val: digit}
    result.Next = sum(nxt1, nxt2, new_carry)
    return result

}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    return sum(l1, l2, 0)
}