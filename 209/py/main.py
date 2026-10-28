def minSubArrayLen(target: int, nums: list[int]) -> int:
    if not nums or sum(nums) < target:
        return 0

    L = R = 0
    m = float("inf")
    total = nums[0]
    while R < len(nums):
        if total >= target:
            m = min(m, R - L + 1)
            total -= nums[L]
            L += 1
            
        else:
            R += 1
            if R < len(nums):
                total += nums[R]

    return m
