package main

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func dfs(root *TreeNode, curr int) int {
    if root == nil {
        return 0
    }
    curr = (curr * 10) + root.Val
    if root.Left == nil && root.Right == nil {
        return curr
    }
    return dfs(root.Left, curr) + dfs(root.Right, curr)
}

func sumNumbers(root *TreeNode) int {
    return dfs(root, 0)
}
