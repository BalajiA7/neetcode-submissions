class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

def insert(root, word):
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        for word in words:
            insert(root, word)

        n = len(board)
        m = len(board[0])
        visited = [[False] * m for i in range(n)]
        res = []

        def dfs(i, j, curr,word):
            if i < 0 or j < 0 or i >= n or j >=m or board[i][j] not in curr.children or visited[i][j]:
                return

            c = board[i][j]

            visited[i][j] = True
            curr = curr.children[c]
            word = word + c
            
            if curr.endOfWord:
                res.append(word)
                curr.endOfWord = False    

            dfs(i, j+1,curr, word)
            dfs(i, j-1,curr, word)
            dfs(i+1, j,curr, word)
            dfs(i-1, j,curr, word)

            visited[i][j] = False
        
        for i in range(n):
            for j in range(m):
                dfs(i, j,root, "")

        return res
        