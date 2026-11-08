class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)

        def merge(i: int = 0) -> str:
            if i >= n1 and i >= n2:
                return ""

            if i >= n2:
                return word1[i:]

            if i >= n1:
                return word2[i:]

            return f"{word1[i]}{word2[i]}{merge(i + 1)}"

        return merge()
