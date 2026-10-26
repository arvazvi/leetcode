package main

type ListNode struct {
    Val int
    Next *ListNode
}

func Pop(head *ListNode) *ListNode {
	var prev, curr *ListNode = nil, head;
	for curr != nil && curr.Next != nil {
		prev = curr
		curr = curr.Next
	}
	prev.Next = nil
	return curr
}

func Prepend(head, node *ListNode) *ListNode {
	node.Next = head
	return node
}

func Len(head *ListNode) int {
	i := 0
	var curr *ListNode = head;
	for curr != nil {
		i++
		curr = curr.Next
	}
	return i
}

func Shift(head *ListNode, k int) *ListNode {
	l := Len(head)
	k = k % l
	for i := 0; i < k; i++ {
		node := Pop(head)
		head = Prepend(head, node)
	}
	
	return head
}
