package main

import "testing"

func TestLCP_Empty(t *testing.T) {
	if got := longestCommonPrefix([]string{}); got != "" {
		t.Fatalf(`longestCommonPrefix([]) = %q; want ""`, got)
	}
}

func TestLCP_Single(t *testing.T) {
	if got := longestCommonPrefix([]string{"apple"}); got != "apple" {
		t.Fatalf(`longestCommonPrefix(["apple"]) = %q; want "apple"`, got)
	}
}

func TestLCP_TwoCommon(t *testing.T) {
	if got := longestCommonPrefix([]string{"flower", "flow", "flight"}); got != "fl" {
		t.Fatalf(`got %q; want "fl"`, got)
	}
}

func TestLCP_NoCommon(t *testing.T) {
	if got := longestCommonPrefix([]string{"dog", "racecar", "car"}); got != "" {
		t.Fatalf(`got %q; want ""`, got)
	}
}

func TestLCP_ExactWholeWord(t *testing.T) {
	if got := longestCommonPrefix([]string{"ab", "a"}); got != "a" {
		t.Fatalf(`got %q; want "a"`, got)
	}
}

func TestLCP_WithEmptyString(t *testing.T) {
	if got := longestCommonPrefix([]string{"a", ""}); got != "" {
		t.Fatalf(`got %q; want ""`, got)
	}
}

func TestLCP_AllSame(t *testing.T) {
	if got := longestCommonPrefix([]string{"abc", "abc", "abc"}); got != "abc" {
		t.Fatalf(`got %q; want "abc"`, got)
	}
}

func TestLCP_PrefixDivergesMidWord(t *testing.T) {
	if got := longestCommonPrefix([]string{"abcde", "abcfg"}); got != "abc" {
		t.Fatalf(`got %q; want "abc"`, got)
	}
}

func TestLCP_TwoEmpty(t *testing.T) {
	if got := longestCommonPrefix([]string{"", ""}); got != "" {
		t.Fatalf(`got %q; want ""`, got)
	}
}

func TestLCP_OneCharPrefix(t *testing.T) {
	if got := longestCommonPrefix([]string{"a", "ab"}); got != "a" {
		t.Fatalf(`got %q; want "a"`, got)
	}
}

func TestLCP_LargeInput(t *testing.T) {
	const n = 1000
	strs := make([]string, n)
	for i := range strs {
		strs[i] = "prefix" + string(rune('a'+(i%26))) + "suffix"
	}
	if got := longestCommonPrefix(strs); got != "prefix" {
		t.Fatalf(`got %q; want "prefix"`, got)
	}
}
