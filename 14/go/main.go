package main

import (
	"strings"
)

type Node struct {
	IsWord    bool
	Children [26]*Node
}

func NewNode() *Node {
	return &Node{}
}

func (n *Node) ChildrenCount() int {
	var count int
	for _, v := range n.Children {
		if v != nil {
			count++
		}
	}

	return count
}

func (n *Node) UniqueNext() int {
	for i, v := range n.Children {
		if v != nil {
			return i
		}
	}
	return -1
}

type Trie struct {
	Root *Node
}

func NewTrie() *Trie {
	return &Trie{Root: NewNode()}
}

func (t *Trie) Add(w string) {
	var root *Node = t.Root
	for _, char := range w {
		idx := char - 'a'
		if root.Children[idx] == nil {
			root.Children[idx] = NewNode()
		}
		root = root.Children[idx]
	}
	root.IsWord = true
}

func (t *Trie) LCP() string {
	var prefix strings.Builder
	root := t.Root
	for root.ChildrenCount() == 1 && !root.IsWord {
		idx := root.UniqueNext()
		prefix.WriteString(string(rune(idx + 'a')))
		root = root.Children[idx]
	}

	return prefix.String()
}

func longestCommonPrefix(strs []string) string {
    t := NewTrie()
	for _, w := range strs {
		t.Add(w)
	}
    return t.LCP()
}