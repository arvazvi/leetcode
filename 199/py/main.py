from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        q = deque([root])
        ans = []
        while q:
            l = len(q)
            nodes = []
            for _ in range(l):
                n = q.popleft()
                nodes.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            if nodes: ans.append(nodes[-1])
        return ans
