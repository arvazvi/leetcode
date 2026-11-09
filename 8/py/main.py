class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        l = len(s)

        while idx < l and s[idx] == " ":
            idx += 1

        sign = 1
        if idx < l and s[idx] == '-':
            sign = -1
            idx += 1
        elif idx < l and s[idx] == '+':
            idx += 1

        ans = 0
        while idx < l and s[idx].isdigit():
            ans = ans * 10 + (ord(s[idx]) - ord('0'))
            idx += 1

        ans *= sign
        ans = max(-2**31, min(ans, 2**31 - 1))
        return ans
