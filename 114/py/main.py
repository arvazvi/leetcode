from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val: int = val
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        stack = []

        def dfs(root):
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