from typing import List

class TrieNode:
    def __init__(self):
        self.is_word: bool = False
        self.children: List['TrieNode'] = [None] * 26

    def add(self, word: str):
        root = self
        for char in word:
            idx = ord(char) - ord("a")
            if not root.children[idx]:
                root.children[idx] = TrieNode()
            root = root.children[idx]
        root.is_word = True


    def search(self, word: str):
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

