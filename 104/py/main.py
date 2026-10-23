class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def dfs(root, length=0):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return length + 1

            return max(dfs(root.left, length + 1), dfs(root.right, length + 1))
        
        return dfs(root)