from __future__ import annotations
from typing import Optional


class TrieNode:
    def __init__(self, value: str):
        self.value = value
        self.next_nodes = dict()
        self.is_end = False
        
    def set_is_end(self):
        self.is_end = True

    def append(self, node: TrieNode):
        if not self.search(node.value):
            self.next_nodes[node.value] = node
    
    def get_node(self, letter: str) -> Optional[TrieNode]:
        return self.next_nodes[letter] if self.search(letter) else None

    def search(self, letter: str) -> bool:
        return True if letter in self.next_nodes else False
