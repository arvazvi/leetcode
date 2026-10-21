import unittest

from main import TrieNode


class TestWordDictionary(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = TrieNode()

    def test_empty_word(self) -> None:
        self.trie.add("")
        self.assertTrue(self.trie.search(""))
        self.assertFalse(self.trie.search("a"))

    def test_add_and_search_exact(self) -> None:
        self.trie.add("bad")
        self.trie.add("dad")
        self.trie.add("mad")
        self.assertTrue(self.trie.search("bad"))
        self.assertTrue(self.trie.search("dad"))
        self.assertTrue(self.trie.search("mad"))

    def test_search_missing(self) -> None:
        self.trie.add("bad")
        self.trie.add("dad")
        self.trie.add("mad")
        self.assertFalse(self.trie.search("pad"))
        self.assertFalse(self.trie.search("bade"))
        self.assertFalse(self.trie.search("ba"))

    def test_prefix_not_word(self) -> None:
        # "bad" anadido, pero "ba" no es una palabra completa.
        self.trie.add("bad")
        self.assertFalse(self.trie.search("ba"))

    def test_wildcard_single(self) -> None:
        self.trie.add("bad")
        self.trie.add("dad")
        self.trie.add("mad")
        self.assertTrue(self.trie.search(".ad"))
        self.assertTrue(self.trie.search("b.d"))
        self.assertTrue(self.trie.search("..d"))

    def test_wildcard_no_match(self) -> None:
        self.trie.add("bad")
        self.trie.add("dad")
        self.trie.add("mad")
        self.assertFalse(self.trie.search("..e"))
        self.assertFalse(self.trie.search("...."))

    def test_wildcard_all(self) -> None:
        self.trie.add("a")
        self.trie.add("ab")
        self.assertTrue(self.trie.search("."))
        self.assertTrue(self.trie.search(".."))
        self.assertFalse(self.trie.search("..."))

    def test_common_prefix(self) -> None:
        # bat / bath / bad comparten prefijo "ba".
        self.trie.add("bat")
        self.trie.add("bath")
        self.trie.add("bad")
        self.assertTrue(self.trie.search("bat"))
        self.assertTrue(self.trie.search("bath"))
        self.assertTrue(self.trie.search("bad"))
        self.assertFalse(self.trie.search("ba"))
        # "ba." coincide con bat y bad, pero no con bath (4 letras).
        self.assertTrue(self.trie.search("ba."))

    def test_wildcard_leading(self) -> None:
        self.trie.add("apple")
        self.trie.add("apply")
        self.trie.add("ample")
        # el wildcard explora todas las ramas en cada nivel.
        self.assertTrue(self.trie.search("....."))
        self.assertTrue(self.trie.search("app.."))
        self.assertTrue(self.trie.search("appl."))
        self.assertTrue(self.trie.search("a.p.."))

    def test_wildcard_at_end(self) -> None:
        self.trie.add("ran")
        self.trie.add("rua")
        self.trie.add("rum")
        self.assertTrue(self.trie.search("r.n"))
        self.assertTrue(self.trie.search("ru."))

    def test_add_duplicates(self) -> None:
        self.trie.add("bad")
        self.trie.add("bad")
        self.assertTrue(self.trie.search("bad"))
        self.assertFalse(self.trie.search("badd"))

    def test_long_word(self) -> None:
        word = "a" * 25
        self.trie.add(word)
        self.assertTrue(self.trie.search(word))
        self.assertTrue(self.trie.search("." * 25))
        self.assertFalse(self.trie.search("." * 26))

    def test_alphabet_coverage(self) -> None:
        # cubre todas las letras del alfabeto.
        for c in "abcdefghijklmnopqrstuvwxyz":
            self.trie.add(c)
        for c in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(self.trie.search(c))
        self.assertTrue(self.trie.search("."))

    def test_search_on_empty_trie(self) -> None:
        self.assertFalse(self.trie.search("anything"))
        self.assertFalse(self.trie.search("."))
        self.assertFalse(self.trie.search(""))


if __name__ == "__main__":
    unittest.main()
