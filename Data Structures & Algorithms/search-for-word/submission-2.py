class Solution:
    def dfs(self,i, j, board,curr,visited,word,n,m):
        if i < 0 or j < 0 or i >= n or j >= m or visited[i][j]:
            return False
        
        curr.append(board[i][j])
        visited[i][j] = True

        if "".join(curr) == word:
            return True
        
        found = (self.dfs(i-1, j, board, curr, visited, word, n, m) or 
        self.dfs(i+1, j, board, curr, visited, word, n, m) or 
        self.dfs(i, j-1, board, curr, visited, word, n, m) or 
        self.dfs(i, j+1, board, curr, visited, word, n, m))

        curr.pop()
        visited[i][j] = False

        return found


    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False for i in range(m)] for i in range(n)]
        curr = []

        for i in range(n):
            for j in range(m):
                if self.dfs(i, j, board, curr, visited, word,n, m):
                    return True

        return False