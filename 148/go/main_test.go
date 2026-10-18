package main

import "testing"

func buildList(keys ...int) *Node {
	if len(keys) == 0 {
		return nil
	}
	head := &Node{Key: keys[0]}
	curr := head
	for _, k := range keys[1:] {
		curr.Next = &Node{Key: k}
		curr = curr.Next
	}
	return head
}

func listToSlice(head *Node) []int {
	var out []int
	for curr := head; curr != nil; curr = curr.Next {
		out = append(out, curr.Key)
	}
	return out
}

func assertSorted(t *testing.T, in []int) {
	t.Helper()
	got := listToSlice(MergeSort(buildList(in...)))
	want := sortedCopy(in)
	if len(got) != len(want) {
		t.Fatalf("MergeSort(%v) = %v; want %v (length mismatch)", in, got, want)
	}
	for i := range want {
		if got[i] != want[i] {
			t.Fatalf("MergeSort(%v) = %v; want %v", in, got, want)
		}
	}
}

func sortedCopy(in []int) []int {
	out := append([]int(nil), in...)
	for i := 1; i < len(out); i++ {
		j := i
		for j > 0 && out[j-1] > out[j] {
			out[j-1], out[j] = out[j], out[j-1]
			j--
		}
	}
	return out
}

func TestMergeSortEmpty(t *testing.T) {
	if head := MergeSort(nil); head != nil {
		t.Fatalf("MergeSort(nil) = %v; want nil", head)
	}
	if got := listToSlice(MergeSort(buildList())); len(got) != 0 {
		t.Fatalf("MergeSort(empty) = %v; want []", got)
	}
}

func TestMergeSortSingleElement(t *testing.T) {
	assertSorted(t, []int{42})
}

func TestMergeSortTwoSorted(t *testing.T) {
	assertSorted(t, []int{1, 2})
}

func TestMergeSortTwoReversed(t *testing.T) {
	assertSorted(t, []int{2, 1})
}

func TestMergeSortAlreadySorted(t *testing.T) {
	assertSorted(t, []int{1, 2, 3, 4, 5, 6, 7})
}

func TestMergeSortReverseOrder(t *testing.T) {
	assertSorted(t, []int{7, 6, 5, 4, 3, 2, 1})
}

func TestMergeSortUnsorted(t *testing.T) {
	assertSorted(t, []int{4, 2, 1, 3, 6, 5})
}

func TestMergeSortWithDuplicates(t *testing.T) {
	assertSorted(t, []int{3, 1, 2, 3, 1, 2, 1})
}

func TestMergeSortWithNegatives(t *testing.T) {
	assertSorted(t, []int{-4, 5, -1, 0, 3, -2})
}

func TestMergeSortEvenLength(t *testing.T) {
	assertSorted(t, []int{8, 4, 6, 2, 7, 5, 3, 1})
}

func TestMergeSortOddLength(t *testing.T) {
	assertSorted(t, []int{9, 7, 5, 3, 1, 8, 6, 4, 2})
}

func TestMergeSortLarge(t *testing.T) {
	const n = 100
	in := make([]int, n)
	for i := range in {
		in[i] = (n - 1) - i // reverse order
	}
	assertSorted(t, in)
}

func TestMergeBothNil(t *testing.T) {
	if got := Merge(nil, nil); got != nil {
		t.Fatalf("Merge(nil, nil) = %v; want nil", got)
	}
}

func TestMergeOneNil(t *testing.T) {
	a := buildList(1, 3, 5)
	if got, want := listToSlice(Merge(a, nil)), []int{1, 3, 5}; !equal(got, want) {
		t.Fatalf("Merge(a, nil) = %v; want %v", got, want)
	}
	b := buildList(2, 4, 6)
	if got, want := listToSlice(Merge(nil, b)), []int{2, 4, 6}; !equal(got, want) {
		t.Fatalf("Merge(nil, b) = %v; want %v", got, want)
	}
}

func TestMergeTwoSorted(t *testing.T) {
	got := listToSlice(Merge(buildList(1, 3, 5), buildList(2, 4, 6)))
	want := []int{1, 2, 3, 4, 5, 6}
	if !equal(got, want) {
		t.Fatalf("Merge = %v; want %v", got, want)
	}
}

func TestMergePreservesDuplicates(t *testing.T) {
	got := listToSlice(Merge(buildList(1, 2, 2), buildList(2, 3)))
	want := []int{1, 2, 2, 2, 3}
	if !equal(got, want) {
		t.Fatalf("Merge = %v; want %v", got, want)
	}
}

func TestSplitPreservesTotal(t *testing.T) {
	head := buildList(1, 2, 3, 4, 5)
	second := Split(head)
	if got, want := listLen(head), 3; got != want {
		t.Fatalf("first half len = %d; want %d", got, want)
	}
	if got, want := listLen(second), 2; got != want {
		t.Fatalf("second half len = %d; want %d", got, want)
	}
	if head.Next != nil && head.Next.Next != nil && head.Next.Next.Next != nil {
		t.Fatalf("first half not terminated; got %v", listToSlice(head))
	}
}

func TestSplitSingle(t *testing.T) {
	head := buildList(1)
	second := Split(head)
	if second != nil {
		t.Fatalf("Split(single) second = %v; want nil", listToSlice(second))
	}
	if head.Next != nil {
		t.Fatalf("Split(single) head.Next = %v; want nil", head.Next)
	}
}

func TestSplitTwo(t *testing.T) {
	head := buildList(1, 2)
	second := Split(head)
	if got, want := listLen(head), 1; got != want {
		t.Fatalf("first half len = %d; want %d", got, want)
	}
	if got, want := listLen(second), 1; got != want {
		t.Fatalf("second half len = %d; want %d", got, want)
	}
}

func equal(a, b []int) bool {
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

func listLen(head *Node) int {
	n := 0
	for curr := head; curr != nil; curr = curr.Next {
		n++
	}
	return n
}
