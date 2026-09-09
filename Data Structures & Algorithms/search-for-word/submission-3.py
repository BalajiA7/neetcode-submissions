class Solution:
    def dfs(self,i, j, board,visited,word,k,n,m):
        if k == len(word):
            return True
            
        if i < 0 or j < 0 or i >= n or j >= m or visited[i][j]:
            return False

        if board[i][j] != word[k]:
            return False
        
        visited[i][j] = True
        
        found = (self.dfs(i-1, j, board, visited, word, k+1, n, m) or 
        self.dfs(i+1, j, board, visited, word, k+1, n, m) or 
        self.dfs(i, j-1, board, visited, word, k+1, n, m) or 
        self.dfs(i, j+1, board, visited, word, k+1, n, m))

        visited[i][j] = False

        return found


    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for i in range(n)]
        curr = []

        for i in range(n):
            for j in range(m):
                if self.dfs(i, j, board, visited, word, 0, n, m):
                    return True

        return False