class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n , m = len(board), len(board[0])
        visited = set()

        def dfs(idx, i, j):
            if idx == len(word):
                return True
            
            if i < 0 or i >= n or j < 0 or j >= m or (i,j) in visited or board[i][j] != word[idx]:
                return False
            
            visited.add((i, j))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                if dfs(idx+1, dr+i, dc+j):
                    visited.remove((i, j))
                    return True
            
            visited.remove((i, j))
            return False
            

        for i in range(n):
            for j in range(m):
                if dfs(0,i,j):
                    return True

        return False        