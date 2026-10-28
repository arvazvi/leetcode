class TrieNode:
    def __init__(self) -> None:
        self.is_word: bool = False
        self.children: list[TrieNode | None] = [None] * 26

    def add(self, word: str) -> None:
        root = self
        for char in word:
            idx = ord(char) - ord("a")
            if not root.children[idx]:
                root.children[idx] = TrieNode()
            root = root.children[idx]
        root.is_word = True


    def search(self, word: str) -> bool:
        root = self
        for i, char in enumerate(word):
            if char == ".":
                for child in root.children:
                    if child and child.search(word[i+1:]): return True
                return False

            idx = ord(char) - ord("a")
            if not root.children[idx]: return False
            root = root.children[idx]
        return root and root.is_word
