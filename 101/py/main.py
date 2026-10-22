class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def mirror(a, b):
            if a and b:
                return mirror(a.left, b.right) and mirror(b.left, a.right) and a.val == b.val
            elif not a and not b:
                return True
            else:
                return False

        if not root:
            return True
        return mirror(root.left, root.right)