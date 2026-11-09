class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = R = 0
        seen: set[str] = set()
        best = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            best = max(best, R - L + 1)

        return best
