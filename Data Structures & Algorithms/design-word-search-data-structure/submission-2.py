class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.isEnd = True
        

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(idx, temp):
            if idx >= n:
                return temp.isEnd

            c = word[idx]
            if c == ".":
                for child in temp.children:
                    if dfs(idx+1, temp.children[child]):
                        return True
            else:
                if c not in temp.children:
                    return False
                if dfs(idx+1, temp.children[c]):
                    return True
            
            return False
        
        return dfs(0, self.root)

            
        # temp = self.root
        # for c in word:
        #     if c == ".":
        #         for child in temp.children:
        #             temp = temp.children[child]
        #     else:
        #         if c not in temp.children:
        #             return False
        #     temp = temp.children[c]
        # return temp.isEnd
        
