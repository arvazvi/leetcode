class Solution:
    def sortColors(self, colors: list[int]) -> None:
        i, j, k = 0, 0, len(colors) - 1
        while j <= k:
            if colors[j] < 1:
                colors[i], colors[j] = colors[j], colors[i]
                i += 1
                j += 1
            elif colors[j] > 1:
                colors[j], colors[k] = colors[k], colors[j]
                k -= 1
            else:
                j += 1
