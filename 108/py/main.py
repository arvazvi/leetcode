class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        L, R = 0, len(nums) - 1

        def process(L, R):
            if L > R:
                return None

            M = (L + R) // 2
            root = TreeNode(nums[M])
            root.left = process(L, M-1)
            root.right = process(M+1, R)
            return root

        return process(L, R)

if __name__ == "__main__":
    nums = list(range(-5, 6))
    s = Solution()
    s.sortedArrayToBST(nums).print()