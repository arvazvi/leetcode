class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        seen: set[tuple[int, int]] = set()

        def dfs(x: int, y: int, idx: int) -> bool:
            if idx == n:
                return True
            if not (0 <= x < rows and 0 <= y < cols):
                return False
            if board[x][y] != word[idx] or (x, y) in seen:
                return False

            seen.add((x, y))
            found = (
                dfs(x, y + 1, idx + 1) or
                dfs(x, y - 1, idx + 1) or
                dfs(x + 1, y, idx + 1) or
                dfs(x - 1, y, idx + 1)
            )
            seen.discard((x, y))
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
