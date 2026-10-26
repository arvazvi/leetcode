package main

import "testing"

func TestRotateSingle(t *testing.T) {
	nums := []int{1}
	rotate(nums, 0)
	assertEqual(t, []int{1}, nums)

	nums = []int{1}
	rotate(nums, 3)
	assertEqual(t, []int{1}, nums)
}

func TestRotateExample1(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	rotate(nums, 3)
	assertEqual(t, []int{5, 6, 7, 1, 2, 3, 4}, nums)
}

func TestRotateExample2(t *testing.T) {
	nums := []int{-1, -100, 3, 99}
	rotate(nums, 2)
	assertEqual(t, []int{3, 99, -1, -100}, nums)
}

func TestRotateKGreaterThanLen(t *testing.T) {
	nums := []int{1, 2, 3}
	rotate(nums, 4)
	assertEqual(t, []int{3, 1, 2}, nums)
}

func TestRotateKZero(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	rotate(nums, 0)
	assertEqual(t, []int{1, 2, 3, 4}, nums)
}

func TestRotateKLen(t *testing.T) {
	nums := []int{1, 2, 3, 4}
	rotate(nums, 4)
	assertEqual(t, []int{1, 2, 3, 4}, nums)
}

func TestRotateTwo(t *testing.T) {
	nums := []int{1, 2}
	rotate(nums, 1)
	assertEqual(t, []int{2, 1}, nums)

	nums = []int{1, 2}
	rotate(nums, 3)
	assertEqual(t, []int{2, 1}, nums)
}

func assertEqual(t *testing.T, want, got []int) {
	t.Helper()
	if len(want) != len(got) {
		t.Fatalf("len mismatch: want %v got %v", want, got)
	}
	for i := range want {
		if want[i] != got[i] {
			t.Errorf("index %d: want %d got %d", i, want[i], got[i])
		}
	}
}
