class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        stack: list[TreeNode] = []

        def dfs(root: TreeNode | None) -> None:
            if root:
                stack.append(root)
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
        dfs(root)
        stack = stack[::-1]
        while stack:
            n = stack.pop()
            n.left = None
            if stack:
                n.right = stack[-1]
