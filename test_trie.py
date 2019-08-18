import unittest
from trie import PrefixTree


class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = PrefixTree()

    def test_trie_size(self):
        self.trie.insert('apple')
        self.assertEqual(self.trie.size(), 6)

    def test_prefix_not_found_as_whole_word(self):
        self.trie.insert('apple')
        self.trie.insert('appreciate')
        self.assertEqual(self.trie.find('app'), None)

    def test_prefix_is_also_whole_word(self):
        self.trie.insert('apple')
        self.trie.insert('appreciate')
        self.trie.insert('app')
        # 10: [app], [appr], [appre], [apprec], [appreci], [apprecia]
        # [appreciat], [appreciate], [appl], and [apple]
        self.assertEqual(self.trie.size(self.trie.find('app')), 10)
        self.assertEqual(self.trie.find('app').is_word, True)

    def test_starts_with(self):
        self.trie.insert('apple')
        self.trie.insert('appreciate')
        self.trie.insert('aposematic')
        self.trie.insert('apoplectic')
        self.trie.insert('appendix')
        self.assertEqual(self.trie.starts_with('app'), ['apple', 'appreciate', 'appendix'])

    def test_starts_with_self(self):
        self.trie.insert('app')
        self.assertEqual(self.trie.starts_with('app'), ['app'])

    def test_bigger_size(self):
        self.trie.insert('bad')
        self.trie.insert('bat')
        self.trie.insert('cat')
        self.trie.insert('cage')
        self.assertEqual(self.trie.size(), 10)

    def test_starts_with_empty_and_no_words(self):
        self.assertEqual(self.trie.starts_with(''), [])

    def test_starts_with_empty_returns_all_words(self):
        self.trie.insert('bad')
        self.trie.insert('bat')
        self.trie.insert('cat')
        self.trie.insert('cage')
        self.assertEqual(self.trie.starts_with(''), ['bad', 'bat', 'cat', 'cage'])


if __name__ == '__main__':
    unittest.main()