package main

import "testing"

func TestIsSubsequence(t *testing.T) {
	tests := []struct {
		name string
		s, t string
		want bool
	}{
		{"example 1", "abc", "ahbgdc", true},
		{"example 2", "axc", "ahbgdc", false},
		{"both empty", "", "", true},
		{"empty s", "", "abc", true},
		{"empty t", "a", "", false},
		{"equal strings", "abc", "abc", true},
		{"s longer than t", "abcd", "abc", false},
		{"wrong order", "ba", "ab", false},
		{"repeated chars", "aaa", "abaca", true},
		{"not enough repeats", "aaaa", "abaca", false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isSubsequence(tt.s, tt.t); got != tt.want {
				t.Errorf("isSubsequence(%q, %q) = %v, want %v", tt.s, tt.t, got, tt.want)
			}
		})
	}
}
