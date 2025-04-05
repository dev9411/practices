from typing import Optional
from tree.trie import Trie
from tree.trie_node import TrieNode


class TrieTraverser:
    def __init__(self):
        self.words = []
        
    def get_all_words(self, trie: Trie) -> list:
        self.__traverse(trie.root, '')
        return self.words
    
    def __traverse(self, node: TrieNode, word: str):
        if node is None:
            self.words.append(word)
            return

        word += node.value
        if node.is_end:
            self.words.append(word)
        
        for next_node in node.next_nodes.values():
            self.__traverse(next_node, word)