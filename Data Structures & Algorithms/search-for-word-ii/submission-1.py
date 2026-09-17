class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        self.root = TrieNode()

        n = len(board)
        m = len(board[0])
        visited = [[False] * m for i in range(n)]
        res = []

        def insert(root, word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True


        def dfs(i, j, curr,temp):
            if curr.endOfWord:
                res.append(temp)
                curr.endOfWord = False
            
            if i < 0 or j < 0 or i >= n or j >=m or visited[i][j]:
                return False

            c = board[i][j]
            if c not in curr.children:
                return False    
            
            visited[i][j] = True
            choices = (dfs(i, j+1,curr.children[c], temp + c) or dfs(i, j-1,curr.children[c], temp + c) or 
                dfs(i+1, j,curr.children[c], temp + c) or dfs(i-1, j,curr.children[c], temp + c))
            visited[i][j] = False

            return choices

        for word in words:
            insert(self.root, word)

        for i in range(n):
            for j in range(m):
                dfs(i, j, self.root, "")

        return res
        