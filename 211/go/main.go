package main

import "fmt"

type Node struct {
	IsWord    bool
	Children [26]*Node
}

func NewNode() *Node {
	return &Node{}
}

func (t *Node) Add(w string) {
	var root *Node = t
	for _, char := range w {
		idx := char - 'a'
		if root.Children[idx] == nil {
			root.Children[idx] = NewNode()
		}
		root = root.Children[idx]
	}
	root.IsWord = true
}

func (t *Node) Search(w string) bool {
	var root *Node = t
	for i, char := range w {
		if char == '.' {
			fmt.Println(".")
			for _, children := range root.Children {
				if children != nil && children.Search(w[i+1:]) {
					return true
				}
			}
			return false
		}

		idx := char - 'a'
		if root.Children[idx] == nil {
			return false
		}
		root = root.Children[idx]
	}
	return root != nil && root.IsWord
}

