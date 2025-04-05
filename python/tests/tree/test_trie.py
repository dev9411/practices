import unittest

from tree.trie import Trie
from tree.trie_traverser import TrieTraverser


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.traverser = TrieTraverser()

    def test_trie_root_node(self):
        self.assertEqual(self.trie.root.value, '')
        
    def test_trie_insert_random_strings(self):
        words = [
            'qwerty',
            'abcdef',
            'mnopqrstu',
            'xyz',
        ]
        for word in words:
            self.trie.insert(word)
        self.assertEqual(
            self.traverser.get_all_words(self.trie),
            words
        )

    def test_trie_insert_overlapping_strings(self):
        words = [
            'qwe',
            'qwerty',
            'qwertymno',
            'qwertymnoxyz',
        ]
        for word in words:
            self.trie.insert(word)
        self.assertEqual(
            self.traverser.get_all_words(self.trie),
            words
        )

    def test_trie_insert_numeric_strings(self):
        words = [
            '1',
            '123',
            '092121',
            '546789765',
        ]
        for word in words:
            self.trie.insert(word)
        self.assertEqual(
            self.traverser.get_all_words(self.trie),
            words
        )
        
    def test_tier_insert_with_duplicates(self):
        words = [
            '123568',
            '123568',
            'qwerty',
            'qwerty',
        ]
        for word in words:
            self.trie.insert(word)
        self.assertListEqual(
            self.traverser.get_all_words(self.trie),
            ['123568', 'qwerty']
        )

    def test_start_with(self):
        words = [
            'qwerty',
            'abcdef',
            'mnopqrstu',
            'xyz',
        ]
        for word in words:
            self.trie.insert(word)
        self.assertTrue(self.trie.start_with('q'))
        self.assertTrue(self.trie.start_with('qwe'))
        self.assertTrue(self.trie.start_with('abcdef'))
        self.assertTrue(self.trie.start_with('mnopqrst'))
        self.assertTrue(self.trie.start_with('mnopqrstu'))
        self.assertTrue(self.trie.start_with('xyz'))
        self.assertTrue(self.trie.start_with('xy'))
        self.assertFalse(self.trie.start_with('xz'))
        self.assertFalse(self.trie.start_with('yz'))
        self.assertFalse(self.trie.start_with('abcdefw'))
        self.assertFalse(self.trie.start_with('rtyugh'))
        self.assertFalse(self.trie.start_with('mnopqrstuoiuyt'))

    def test_search(self):
        words = [
            'qwerty',
            'abcdef',
            'mnopqrstu',
            'xyz',
        ]
        for word in words:
            self.trie.insert(word)
        
        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertFalse(self.trie.search('q'))
        self.assertFalse(self.trie.search('qwe'))
        self.assertFalse(self.trie.search('mnopqrst'))
        self.assertFalse(self.trie.search('xy'))
        self.assertFalse(self.trie.search('xz'))
        self.assertFalse(self.trie.search('yz'))
        self.assertFalse(self.trie.search('abcdefw'))
        self.assertFalse(self.trie.search('rtyugh'))
        self.assertFalse(self.trie.search('mnopqrstuoiuyt'))
