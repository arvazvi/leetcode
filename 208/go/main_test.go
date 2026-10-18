package main

import "testing"

func TestTrie_SearchNotFound(t *testing.T) {
	tr := NewTrie()
	if tr.Search("apple") {
		t.Fatal("expected Search on empty trie to be false")
	}
}

func TestTrie_InsertAndSearch(t *testing.T) {
	tr := NewTrie()
	tr.Add("apple")
	if !tr.Search("apple") {
		t.Fatal("Search(apple) should be true after Add(apple)")
	}
}

func TestTrie_SearchPrefixNotWord(t *testing.T) {
	tr := NewTrie()
	tr.Add("apple")
	if tr.Search("app") {
		t.Fatal(`Search("app") should be false; "app" is a prefix, not a word`)
	}
}

func TestTrie_StartsWith(t *testing.T) {
	tr := NewTrie()
	tr.Add("apple")
	if !tr.StartsWith("app") {
		t.Fatal(`StartsWith("app") should be true after Add("apple")`)
	}
}

func TestTrie_StartsWithExact(t *testing.T) {
	tr := NewTrie()
	tr.Add("apple")
	if !tr.StartsWith("apple") {
		t.Fatal(`StartsWith("apple") should be true`)
	}
}

func TestTrie_StartsWithNotFound(t *testing.T) {
	tr := NewTrie()
	tr.Add("apple")
	if tr.StartsWith("apx") {
		t.Fatal(`StartsWith("apx") should be false`)
	}
}

func TestTrie_MultipleWords(t *testing.T) {
	tr := NewTrie()
	words := []string{"apple", "app", "apricot", "banana"}
	for _, w := range words {
		tr.Add(w)
	}
	for _, w := range words {
		if !tr.Search(w) {
			t.Fatalf("Search(%q) should be true", w)
		}
	}
}

func TestTrie_PrefixDoesNotImplyWord(t *testing.T) {
	tr := NewTrie()
	tr.Add("app")
	tr.Add("apple")
	if !tr.Search("app") {
		t.Fatal(`Search("app") should be true`)
	}
	if !tr.Search("apple") {
		t.Fatal(`Search("apple") should be true`)
	}
	if tr.Search("ap") {
		t.Fatal(`Search("ap") should be false`)
	}
}

func TestTrie_SearchEmpty(t *testing.T) {
	tr := NewTrie()
	if tr.Search("") {
		t.Fatal(`Search("") on empty trie should be false`)
	}
}

func TestTrie_EmptyStringInsertAndSearch(t *testing.T) {
	tr := NewTrie()
	tr.Add("")
	if !tr.Search("") {
		t.Fatal(`Search("") should be true after Add("")`)
	}
}

func TestTrie_StartsWithEmpty(t *testing.T) {
	tr := NewTrie()
	if !tr.StartsWith("") {
		t.Fatal(`StartsWith("") on empty trie should be true (empty prefix of everything)`)
	}
}

func TestTrie_LongerPrefixNotFound(t *testing.T) {
	tr := NewTrie()
	tr.Add("app")
	if tr.StartsWith("apple") {
		t.Fatal(`StartsWith("apple") should be false when only "app" was added`)
	}
}
