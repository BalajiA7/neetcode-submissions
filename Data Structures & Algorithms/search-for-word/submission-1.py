class Solution:
    def dfs(self,i, j, board,curr,visited,word,n,m):
        if i < 0 or j < 0 or i >= n or j >= m or visited[i][j]:
            return False
        
        curr.append(board[i][j])
        visited[i][j] = True

        if "".join(curr) == word:
            return True
        
        # move Up
        a = self.dfs(i-1, j, board, curr, visited, word, n, m)
        if a:
            return True
        
        # move Down
        b = self.dfs(i+1, j, board, curr, visited, word, n, m)
        if b:
            return True
        
        # move left
        c = self.dfs(i, j-1, board, curr, visited, word, n, m)
        if c:
            return True
        
        # move right
        d = self.dfs(i, j+1, board, curr, visited, word, n, m)
        if d:
            return True
        
        curr.pop()
        visited[i][j] = False
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False for i in range(m)] for i in range(n)]
        curr = []

        for i in range(n):
            hasFound = False
            for j in range(m):
                hasFound = self.dfs(i, j, board, curr, visited, word,n, m)
                if hasFound:
                    return True

        return False