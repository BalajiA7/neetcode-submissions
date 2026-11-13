class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n , m = len(board), len(board[0])
        visited = set()

        def dfs(idx, i, j):
            if idx == len(word):
                return True
            
            visited.add((i, j))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                row = dr+i
                col = dc+j

                if row >=0 and row < n and col >=0 and col < m and (row, col) not in visited and board[row][col] == word[idx]:
                    if dfs(idx+1, row, col):
                        return True
            
            visited.remove((i, j))
            return False
            

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(1,i,j):
                        return True
        return False        