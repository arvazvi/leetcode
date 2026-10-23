package main

import "testing"

func buildTree(values []interface{}) *TreeNode {
	if len(values) == 0 {
		return nil
	}
	root := &TreeNode{Val: values[0].(int)}
	queue := []*TreeNode{root}
	i := 1
	for len(queue) > 0 && i < len(values) {
		node := queue[0]
		queue = queue[1:]
		if i < len(values) && values[i] != nil {
			node.Left = &TreeNode{Val: values[i].(int)}
			queue = append(queue, node.Left)
		}
		i++
		if i < len(values) && values[i] != nil {
			node.Right = &TreeNode{Val: values[i].(int)}
			queue = append(queue, node.Right)
		}
		i++
	}
	return root
}

func TestSumNumbers_Empty(t *testing.T) {
	if got := sumNumbers(nil); got != 0 {
		t.Fatalf(`sumNumbers(nil) = %d; want 0`, got)
	}
}

func TestSumNumbers_Single(t *testing.T) {
	root := &TreeNode{Val: 5}
	if got := sumNumbers(root); got != 5 {
		t.Fatalf(`got %d; want 5`, got)
	}
}

func TestSumNumbers_LeetCode1(t *testing.T) {
	// [1,2,3] -> 12 + 13 = 25
	root := buildTree([]interface{}{1, 2, 3})
	if got := sumNumbers(root); got != 25 {
		t.Fatalf(`got %d; want 25`, got)
	}
}

func TestSumNumbers_LeetCode2(t *testing.T) {
	// [4,9,0,5,1] -> 495 + 491 + 40 = 1026
	root := buildTree([]interface{}{4, 9, 0, 5, 1})
	if got := sumNumbers(root); got != 1026 {
		t.Fatalf(`got %d; want 1026`, got)
	}
}

func TestSumNumbers_LeftSkewed(t *testing.T) {
	// [1,2,None,3] -> 123
	root := buildTree([]interface{}{1, 2, nil, 3})
	if got := sumNumbers(root); got != 123 {
		t.Fatalf(`got %d; want 123`, got)
	}
}

func TestSumNumbers_RightSkewed(t *testing.T) {
	// [1,None,2,None,3] -> 123
	root := buildTree([]interface{}{1, nil, 2, nil, 3})
	if got := sumNumbers(root); got != 123 {
		t.Fatalf(`got %d; want 123`, got)
	}
}

func TestSumNumbers_TwoLeaves(t *testing.T) {
	// [1,2,3] -> 12 + 13 = 25
	root := buildTree([]interface{}{1, 2, 3})
	if got := sumNumbers(root); got != 25 {
		t.Fatalf(`got %d; want 25`, got)
	}
}

func TestSumNumbers_ThreeLevels(t *testing.T) {
	// [1,2,3,4,5,6,7] -> 124 + 125 + 136 + 137 = 522
	root := buildTree([]interface{}{1, 2, 3, 4, 5, 6, 7})
	if got := sumNumbers(root); got != 522 {
		t.Fatalf(`got %d; want 522`, got)
	}
}

func TestSumNumbers_ZeroRoot(t *testing.T) {
	// [0,1,2] -> 1 + 2 = 3
	root := buildTree([]interface{}{0, 1, 2})
	if got := sumNumbers(root); got != 3 {
		t.Fatalf(`got %d; want 3`, got)
	}
}

func TestSumNumbers_AllZeros(t *testing.T) {
	// [0,0,0] -> 0 + 0 = 0
	root := buildTree([]interface{}{0, 0, 0})
	if got := sumNumbers(root); got != 0 {
		t.Fatalf(`got %d; want 0`, got)
	}
}

func TestSumNumbers_DeepLeft(t *testing.T) {
	// [1,2,None,3,None,4] -> 1234
	root := buildTree([]interface{}{1, 2, nil, 3, nil, 4})
	if got := sumNumbers(root); got != 1234 {
		t.Fatalf(`got %d; want 1234`, got)
	}
}

func TestSumNumbers_Unbalanced(t *testing.T) {
	// [4,9,0,5,1] -> 495 + 491 + 40 = 1026
	root := buildTree([]interface{}{4, 9, 0, 5, 1})
	if got := sumNumbers(root); got != 1026 {
		t.Fatalf(`got %d; want 1026`, got)
	}
}

func TestSumNumbers_OneChild(t *testing.T) {
	// [1,2] -> 12
	root := buildTree([]interface{}{1, 2})
	if got := sumNumbers(root); got != 12 {
		t.Fatalf(`got %d; want 12`, got)
	}
}

func TestSumNumbers_Large(t *testing.T) {
	// [9,9,9,9,9,9,9,9,9,9] (full 4-level tree)
	// paths: 9999 * 8 leaves = but easier: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	// -> 1248+1249+12510+12511+13612+13613+13614+13615
	// too complex; use simple: [1,2,3,4] -> 124 + 13 = 137
	root := buildTree([]interface{}{1, 2, 3, 4})
	if got := sumNumbers(root); got != 137 {
		t.Fatalf(`got %d; want 137`, got)
	}
}
