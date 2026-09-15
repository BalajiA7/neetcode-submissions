class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
                

    def search(self, word: str) -> bool:
        curr = self.root

        def recursiveSearch(idx,curr):
            if idx == len(word):
                return curr.endOfWord
            
            c = word[idx]

            if c == ".":
                for child in curr.children.values():
                    if recursiveSearch(idx+1, child):
                        return True
                return False   
            else:
                if c not in curr.children:
                    return False

                return recursiveSearch(idx+1, curr.children[c])
        
            
        return recursiveSearch(0,curr)
                

        
