package main

import (
	"fmt"
	"strings"
)

type Node struct {
	IsWord    bool
	Children [26]*Node
}

func NewNode() *Node {
	return &Node{}
}

func (n *Node) HasOne() (bool, int) {
	var count int
	var lastSeen int = -1
	for i, v := range n.Children {
		if v != nil {
			count++
			lastSeen = i
		}
	}

	return count == 1, lastSeen
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
	hasOne, idx := root.HasOne()

	for hasOne && !root.IsWord {
		prefix.WriteString(string(rune(idx + 'a')))
		root = root.Children[idx]
		hasOne, idx = root.HasOne()
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

func main() {
	var wrds = []string{"flower", "flowershop", }
	fmt.Println(longestCommonPrefix(wrds))
}