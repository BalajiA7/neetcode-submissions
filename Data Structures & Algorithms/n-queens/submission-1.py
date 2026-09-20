class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        col = set()
        right = set()
        left = set()
        res = []

        def valid(r,c):
            if c in col:
                return False
            if (r+c) in right:
                return False
            if (r-c) in left:
                return False

            return True
        
        def dfs(r):
            if r == n:
                formatedBoard = ["".join(row) for row in board]
                res.append(formatedBoard)
                return

            for c in range(n):
                if valid(r,c):
                    col.add(c)
                    right.add((r+c))
                    left.add((r-c))
                    board[r][c] = "Q"
                    dfs(r+1)
                    col.remove(c)
                    right.remove((r+c))
                    left.remove((r-c))
                    board[r][c] = "."


        dfs(0)

        
        return res
        