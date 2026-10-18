package main

type Node struct {
	Char     rune
	IsEnd    bool
	Children [26]*Node
}

func NewNode(c rune) *Node {
	return &Node{Char: c}
}

type Trie struct {
	Root *Node
}

func NewTrie() *Trie {
	return &Trie{Root: NewNode(' ')}
}


func (t *Trie) Add(w string) {
	var root *Node = t.Root
	for _, char := range w {
		idx := char - 'a'
		if root.Children[idx] == nil {
			root.Children[idx] = NewNode(char)
		}
		root = root.Children[idx]
	}
	root.IsEnd = true
}

func (t *Trie) Search(w string) bool {
	var root *Node = t.Root
	for _, char := range w {
		idx := char - 'a'
		if root.Children[idx] == nil {
			return false
		}
		root = root.Children[idx]
	}
	return root.IsEnd
}

func (t *Trie) StartsWith(w string) bool {
	var root *Node = t.Root
	for _, char := range w {
		idx := char - 'a'
		if root.Children[idx] == nil {
			return false
		}
		root = root.Children[idx]
	}
	return true
}

