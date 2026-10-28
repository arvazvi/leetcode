class Trie:
    def __init__(self) -> None:
        self.is_word: bool = False
        self.children: dict[int, Trie] = {}

    def add(self, word: str) -> None:
        root = self
        for char in word:
            idx = ord(char) - ord('a')
            if not root.children.get(idx):
                root.children[idx] = Trie()
            root = root.children[idx]
        root.is_word = True

    def search_char(self, char: str) -> Trie | None:
        return self.children.get(ord(char) - ord('a'))

def dfs(x: int, y: int, board: list[list[str]], root: Trie, seen: set[tuple[int, int]], ans: list[str], path: list[str]) -> None:
    rows = len(board)
    cols = len(board[0])

    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if (x, y) in seen:
        return

    ch = board[x][y]
    idx = ord(ch) - ord('a')
    child = root.search_char(ch)
    if child is None:
        return

    seen.add((x, y))
    path.append(ch)

    if child.is_word:
        ans.append(''.join(path))
        child.is_word = False

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(x + dx, y + dy, board, child, seen, ans, path)

    if not child.is_word and not any(child.children.values()):
        root.children[idx] = None

    seen.discard((x, y))
    path.pop()


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        rows = len(board)
        cols = len(board[0])

        if rows == 0 or cols == 0: return []

        trie = Trie()
        for word in words:
            trie.add(word)
            
        ans: list[str] = []
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, board, trie, set(), ans, [])

        return ans
