package main

import (
	"slices"
	"testing"
)

func TestTwoSum(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		target int
		want   []int
	}{
		{"example 1", []int{2, 7, 11, 15}, 9, []int{0, 1}},
		{"example 2", []int{3, 2, 4}, 6, []int{1, 2}},
		{"example 3", []int{3, 3}, 6, []int{0, 1}},
		{"negatives", []int{-1, -2, -3, -4, -5}, -8, []int{2, 4}},
		{"zeros", []int{0, 4, 3, 0}, 0, []int{0, 3}},
		{"mixed signs", []int{-3, 4, 3, 90}, 0, []int{0, 2}},
		{"no same element twice", []int{5, 1, 5}, 10, []int{0, 2}},
	}
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			got := twoSum(tc.nums, tc.target)
			slices.Sort(got)
			if !slices.Equal(got, tc.want) {
				t.Fatalf("twoSum(%v, %d) = %v, want %v", tc.nums, tc.target, got, tc.want)
			}
		})
	}
}

func TestTwoSumNoSolution(t *testing.T) {
	if got := twoSum([]int{1, 2, 3}, 100); got != nil {
		t.Fatalf("got %v, want nil", got)
	}
}
