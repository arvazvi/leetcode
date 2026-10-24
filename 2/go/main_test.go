package main

import "testing"

// buildList converts a slice of digits into a singly linked list.
func buildList(digits []int) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	for _, d := range digits {
		cur.Next = &ListNode{Val: d}
		cur = cur.Next
	}
	return dummy.Next
}

// toSlice converts a singly linked list back into a slice of digits.
func toSlice(head *ListNode) []int {
	var out []int
	for cur := head; cur != nil; cur = cur.Next {
		out = append(out, cur.Val)
	}
	return out
}

func TestAddTwoNumbers_Example1(t *testing.T) {
	// 342 + 465 = 807
	l1 := buildList([]int{2, 4, 3})
	l2 := buildList([]int{5, 6, 4})
	got := addTwoNumbers(l1, l2)
	want := []int{7, 0, 8}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_Example2(t *testing.T) {
	// 0 + 0 = 0
	l1 := buildList([]int{0})
	l2 := buildList([]int{0})
	got := addTwoNumbers(l1, l2)
	want := []int{0}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_Example3(t *testing.T) {
	// 9999999 + 9999 = 10009998
	l1 := buildList([]int{9, 9, 9, 9, 9, 9, 9})
	l2 := buildList([]int{9, 9, 9, 9})
	got := addTwoNumbers(l1, l2)
	want := []int{8, 9, 9, 9, 0, 0, 0, 1}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_DifferentLengths(t *testing.T) {
	// 99 + 1 = 100
	l1 := buildList([]int{9, 9})
	l2 := buildList([]int{1})
	got := addTwoNumbers(l1, l2)
	want := []int{0, 0, 1}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_BothEmpty(t *testing.T) {
	got := addTwoNumbers(nil, nil)
	if got != nil {
		t.Fatalf("got %v, want nil", got)
	}
}

func TestAddTwoNumbers_OneEmpty(t *testing.T) {
	// 0 + 123 = 123
	l2 := buildList([]int{3, 2, 1})
	got := addTwoNumbers(nil, l2)
	want := []int{3, 2, 1}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_CarryOnly(t *testing.T) {
	// 5 + 5 = 10
	l1 := buildList([]int{5})
	l2 := buildList([]int{5})
	got := addTwoNumbers(l1, l2)
	want := []int{0, 1}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_LargeCarry(t *testing.T) {
	// 9 + 9 = 18
	l1 := buildList([]int{9})
	l2 := buildList([]int{9})
	got := addTwoNumbers(l1, l2)
	want := []int{8, 1}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_AllNines(t *testing.T) {
	// 999 + 999 = 1998
	l1 := buildList([]int{9, 9, 9})
	l2 := buildList([]int{9, 9, 9})
	got := addTwoNumbers(l1, l2)
	want := []int{8, 9, 9, 1}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func TestAddTwoNumbers_ZerosInMiddle(t *testing.T) {
	// 101 + 202 = 303
	l1 := buildList([]int{1, 0, 1})
	l2 := buildList([]int{2, 0, 2})
	got := addTwoNumbers(l1, l2)
	want := []int{3, 0, 3}
	if !equalSlice(toSlice(got), want) {
		t.Fatalf("got %v, want %v", toSlice(got), want)
	}
}

func equalSlice(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
