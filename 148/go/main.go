package main

import "fmt"

type Node struct {
	Key  int
	Next *Node
}

func (head *Node) Peek() {
	curr := head
	for curr != nil {
		fmt.Printf("%d->", curr.Key)
		curr = curr.Next
	}
	fmt.Println()
}

func Split(head *Node) *Node {
	slow, fast := head, head

	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		if fast != nil {
			slow = slow.Next
		}
	}
	second := slow.Next
	slow.Next = nil
	return second
}

func Merge(n1, n2 *Node) *Node {
	if n1 == nil {
		return n2
	}

	if n2 == nil {
		return n1
	}

	if n1.Key <= n2.Key {
		n1.Next = Merge(n1.Next, n2)
		return n1
	}
	n2.Next = Merge(n1, n2.Next)
	return n2
}

func MergeSort(head *Node) *Node {
	if head == nil || head.Next == nil {
		return head
	}

	second := Split(head)
	head, second = MergeSort(head), MergeSort(second)
	return Merge(head, second)
}
