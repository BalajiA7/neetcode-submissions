class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.Trie = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.Trie
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.isEnd = True

    def search(self, word: str) -> bool:
        temp = self.Trie
        for c in word:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        temp = self.Trie
        for c in prefix:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return True
        