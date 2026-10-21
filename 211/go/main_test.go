package main

import "testing"

func TestSearchEmptyTrie(t *testing.T) {
	tr := NewNode()
	if tr.Search("anything") {
		t.Fatal("Search on empty trie should be false")
	}
	if tr.Search(".") {
		t.Fatal(`Search(".") on empty trie should be false`)
	}
	if tr.Search("") {
		t.Fatal(`Search("") on empty trie should be false`)
	}
}

func TestEmptyWord(t *testing.T) {
	tr := NewNode()
	tr.Add("")
	if !tr.Search("") {
		t.Fatal(`Search("") should be true after Add("")`)
	}
	if tr.Search("a") {
		t.Fatal(`Search("a") should be false`)
	}
}

func TestAddAndSearchExact(t *testing.T) {
	tr := NewNode()
	tr.Add("bad")
	tr.Add("dad")
	tr.Add("mad")
	if !tr.Search("bad") {
		t.Fatal(`Search("bad") should be true`)
	}
	if !tr.Search("dad") {
		t.Fatal(`Search("dad") should be true`)
	}
	if !tr.Search("mad") {
		t.Fatal(`Search("mad") should be true`)
	}
}

func TestSearchMissing(t *testing.T) {
	tr := NewNode()
	tr.Add("bad")
	tr.Add("dad")
	tr.Add("mad")
	if tr.Search("pad") {
		t.Fatal(`Search("pad") should be false`)
	}
	if tr.Search("bade") {
		t.Fatal(`Search("bade") should be false`)
	}
	if tr.Search("ba") {
		t.Fatal(`Search("ba") should be false`)
	}
}

func TestPrefixNotWord(t *testing.T) {
	tr := NewNode()
	tr.Add("bad")
	if tr.Search("ba") {
		t.Fatal(`Search("ba") should be false; "ba" is a prefix, not a word`)
	}
}

func TestWildcardSingle(t *testing.T) {
	tr := NewNode()
	tr.Add("bad")
	tr.Add("dad")
	tr.Add("mad")
	if !tr.Search(".ad") {
		t.Fatal(`Search(".ad") should be true`)
	}
	if !tr.Search("b.d") {
		t.Fatal(`Search("b.d") should be true`)
	}
	if !tr.Search("..d") {
		t.Fatal(`Search("..d") should be true`)
	}
}

func TestWildcardNoMatch(t *testing.T) {
	tr := NewNode()
	tr.Add("bad")
	tr.Add("dad")
	tr.Add("mad")
	if tr.Search("..e") {
		t.Fatal(`Search("..e") should be false`)
	}
	if tr.Search("....") {
		t.Fatal(`Search("....") should be false`)
	}
}

func TestWildcardAll(t *testing.T) {
	tr := NewNode()
	tr.Add("a")
	tr.Add("ab")
	if !tr.Search(".") {
		t.Fatal(`Search(".") should be true`)
	}
	if !tr.Search("..") {
		t.Fatal(`Search("..") should be true`)
	}
	if tr.Search("...") {
		t.Fatal(`Search("...") should be false`)
	}
}

func TestCommonPrefix(t *testing.T) {
	tr := NewNode()
	tr.Add("bat")
	tr.Add("bath")
	tr.Add("bad")
	if !tr.Search("bat") {
		t.Fatal(`Search("bat") should be true`)
	}
	if !tr.Search("bath") {
		t.Fatal(`Search("bath") should be true`)
	}
	if !tr.Search("bad") {
		t.Fatal(`Search("bad") should be true`)
	}
	if tr.Search("ba") {
		t.Fatal(`Search("ba") should be false`)
	}
	if !tr.Search("ba.") {
		t.Fatal(`Search("ba.") should be true (matches bat and bad)`)
	}
}

func TestWildcardLeading(t *testing.T) {
	tr := NewNode()
	tr.Add("apple")
	tr.Add("apply")
	tr.Add("ample")
	if !tr.Search(".....") {
		t.Fatal(`Search(".....") should be true`)
	}
	if !tr.Search("app..") {
		t.Fatal(`Search("app..") should be true`)
	}
	if !tr.Search("appl.") {
		t.Fatal(`Search("appl.") should be true`)
	}
	if !tr.Search("a.p..") {
		t.Fatal(`Search("a.p..") should be true (matches apple)`)
	}
}

func TestWildcardAtEnd(t *testing.T) {
	tr := NewNode()
	tr.Add("ran")
	tr.Add("rua")
	tr.Add("rum")
	if !tr.Search("r.n") {
		t.Fatal(`Search("r.n") should be true (matches ran)`)
	}
	if !tr.Search("ru.") {
		t.Fatal(`Search("ru.") should be true (matches rua and rum)`)
	}
}

func TestAddDuplicates(t *testing.T) {
	tr := NewNode()
	tr.Add("bad")
	tr.Add("bad")
	if !tr.Search("bad") {
		t.Fatal(`Search("bad") should be true`)
	}
	if tr.Search("badd") {
		t.Fatal(`Search("badd") should be false`)
	}
}

func TestLongWord(t *testing.T) {
	word := ""
	for i := 0; i < 25; i++ {
		word += "a"
	}
	tr := NewNode()
	tr.Add(word)
	if !tr.Search(word) {
		t.Fatal("Search of long word should be true")
	}
	dots := ""
	for i := 0; i < 25; i++ {
		dots += "."
	}
	if !tr.Search(dots) {
		t.Fatal(`Search("....." 25x) should be true`)
	}
	dots += "."
	if tr.Search(dots) {
		t.Fatal(`Search with 26 dots should be false`)
	}
}

func TestAlphabetCoverage(t *testing.T) {
	tr := NewNode()
	for c := 'a'; c <= 'z'; c++ {
		tr.Add(string(c))
	}
	for c := 'a'; c <= 'z'; c++ {
		if !tr.Search(string(c)) {
			t.Fatalf("Search(%q) should be true", string(c))
		}
	}
	if !tr.Search(".") {
		t.Fatal(`Search(".") should be true`)
	}
}
