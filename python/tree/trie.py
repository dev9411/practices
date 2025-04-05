from tree.trie_node import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode('')
        
    def insert(self, word: str):
        current_node = self.root
        for letter in word:
            if not current_node.search(letter):
                current_node.append(TrieNode(letter))
            current_node = current_node.get_node(letter)
        current_node.set_is_end()
        
    def start_with(self, prefix: str) -> bool:
        current_node = self.root
        for letter in prefix:
            if not current_node.search(letter):
                return False
            current_node = current_node.get_node(letter)
        return True

    def search(self, word: str) -> bool:
        current_node = self.root
        for letter in word:
            if not current_node.search(letter):
                return False
            current_node = current_node.get_node(letter)
        return current_node.is_end
