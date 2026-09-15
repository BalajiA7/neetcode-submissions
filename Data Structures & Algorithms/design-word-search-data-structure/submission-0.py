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

        def recursiveSearch(idx,curr,word):
            if idx == len(word):
                return curr.endOfWord
            
            c = word[idx]

            if c == ".":
                for char in range(ord('a'), ord('z') +1):
                    ch = chr(char)
                    if ch in curr.children:
                        if recursiveSearch(idx+1,curr.children[ch], word):
                            return True
                return False   
            else:
                if c not in curr.children:
                    return False

                return recursiveSearch(idx+1, curr.children[c], word)
        
            
        return recursiveSearch(0,curr, word)
                

        
