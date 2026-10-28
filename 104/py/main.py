from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val: int = val
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def dfs(root: TreeNode | None, length: int = 0) -> int:
            if not root:
                return 0
            
            if not root.left and not root.right:
                return length + 1

            return max(dfs(root.left, length + 1), dfs(root.right, length + 1))
        
        return dfs(root)