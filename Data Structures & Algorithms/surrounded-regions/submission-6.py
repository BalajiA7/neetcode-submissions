class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(r,c):            
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    dfs(nr,nc)
        
        
        # First row
        for c in range(m):
            if board[0][c] == "O":
                board[0][c] = "T"
                dfs(0, c)
        
        # last row
        for c in range(m):
            if board[n-1][c] == "O":
                board[n-1][c] = "T"
                dfs(n-1, c)
        
        # first col
        for r in range(n):
            if board[r][0] == "O":
                board[r][0] = "T"
                dfs(r, 0)
        
        # last col
        for r in range(n):
            if board[r][m-1] == "O":
                board[r][m-1] = "T"
                dfs(r, m-1)
        
        # Loop over and change not visted 'O' into 'X'
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Loop over and change visted 'T' into  'O'
        for r in range(n):
            for c in range(m):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        

        