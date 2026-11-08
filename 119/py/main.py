from functools import cache

class Solution:
    @cache
    def getRow(self, rowIndex: int) -> list[int]:
        base = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        if rowIndex < 5:
            return base[rowIndex]

        prev = self.getRow(rowIndex - 1)
        new: list[int] = []
        i = 0
        while i < len(prev) - 1:
            new.append(prev[i] + prev[i + 1])
            i += 1
        return [1] + new + [1]
