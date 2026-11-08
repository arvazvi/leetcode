from functools import cache

class Solution:
    @cache
    def generate(self, numRows: int) -> list[list[int]]:
        base: list[list[int]] = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        if numRows < 6:
            return base[:numRows]

        for i in range(5, numRows):
            prev: list[int] = base[-1]
            new: list[int] = []
            i = 0
            while i < len(prev) - 1:
                new.append(prev[i] + prev[i + 1])
                i += 1
            base.append([1] + new + [1])
        return base