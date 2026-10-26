package main

import "testing"

// buildList converts a slice of ints into a singly linked list.
func buildList(vals []int) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	for _, v := range vals {
		cur.Next = &ListNode{Val: v}
		cur = cur.Next
	}
	return dummy.Next
}

// toSlice converts a singly linked list back into a slice of ints.
func toSlice(head *ListNode) []int {
	var out []int
	for cur := head; cur != nil; cur = cur.Next {
		out = append(out, cur.Val)
	}
	return out
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

func assertShift(t *testing.T, vals []int, k int, want []int) {
	t.Helper()
	head := buildList(vals)
	got := toSlice(Shift(head, k))
	if !equalSlice(got, want) {
		t.Fatalf("Shift(%v, %d) = %v; want %v", vals, k, got, want)
	}
}

func TestShift_Example1(t *testing.T) {
	// [1,2,3,4,5], k=2 -> [4,5,1,2,3]
	assertShift(t, []int{1, 2, 3, 4, 5}, 2, []int{4, 5, 1, 2, 3})
}

func TestShift_Example2(t *testing.T) {
	// [0,1,2], k=4 -> 4%3=1 -> [2,0,1]
	assertShift(t, []int{0, 1, 2}, 4, []int{2, 0, 1})
}

func TestShift_ZeroRotation(t *testing.T) {
	// k=0 returns the list unchanged.
	assertShift(t, []int{1, 2, 3, 4, 5}, 0, []int{1, 2, 3, 4, 5})
}

func TestShift_KEqualsLength(t *testing.T) {
	// k == len -> k%len == 0, no rotation.
	assertShift(t, []int{1, 2, 3}, 3, []int{1, 2, 3})
}

func TestShift_KMultipleOfLength(t *testing.T) {
	// k=6, len=3 -> 6%3==0, no rotation.
	assertShift(t, []int{1, 2, 3}, 6, []int{1, 2, 3})
}

func TestShift_SingleNodeAnyK(t *testing.T) {
	// Single node: k%1 == 0, always returns the same node.
	assertShift(t, []int{42}, 5, []int{42})
	assertShift(t, []int{42}, 0, []int{42})
}

func TestShift_TwoNodesRotateOnce(t *testing.T) {
	// [1,2], k=1 -> [2,1]
	assertShift(t, []int{1, 2}, 1, []int{2, 1})
}

func TestShift_TwoNodesFullRotation(t *testing.T) {
	// [1,2], k=2 -> 2%2==0, unchanged.
	assertShift(t, []int{1, 2}, 2, []int{1, 2})
}

func TestShift_RotateAllButOne(t *testing.T) {
	// [1,2,3,4,5], k=4 -> [2,3,4,5,1]
	assertShift(t, []int{1, 2, 3, 4, 5}, 4, []int{2, 3, 4, 5, 1})
}

func TestShift_LargeK(t *testing.T) {
	// [1,2,3,4,5], k=2000000000 -> 2000000000 % 5 == 0, unchanged.
	assertShift(t, []int{1, 2, 3, 4, 5}, 2000000000, []int{1, 2, 3, 4, 5})
}

func TestLen(t *testing.T) {
	cases := []struct {
		vals []int
		want int
	}{
		{[]int{1, 2, 3}, 3},
		{[]int{42}, 1},
		{[]int{}, 0},
	}
	for _, c := range cases {
		if got := Len(buildList(c.vals)); got != c.want {
			t.Errorf("Len(%v) = %d; want %d", c.vals, got, c.want)
		}
	}
}

func TestPop_LastNode(t *testing.T) {
	// [1,2,3] -> Pop returns 3, list becomes [1,2]
	head := buildList([]int{1, 2, 3})
	node := Pop(head)
	if node == nil || node.Val != 3 {
		t.Fatalf("Pop returned %v; want node with Val 3", node)
	}
	if !equalSlice(toSlice(head), []int{1, 2}) {
		t.Fatalf("after Pop, list = %v; want [1 2]", toSlice(head))
	}
}

func TestPrepend(t *testing.T) {
	head := buildList([]int{1, 2})
	node := &ListNode{Val: 0}
	result := Prepend(head, node)
	if !equalSlice(toSlice(result), []int{0, 1, 2}) {
		t.Fatalf("Prepend = %v; want [0 1 2]", toSlice(result))
	}
}
