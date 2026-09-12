class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr =  [['.' for x in range(n)] for x in range(n)]

        def isValid(i, j, curr):
            # check col
            for k in range(i):
                if curr[k][j] == 'Q':
                    return False
                    
            # check upper left diagonal
            row = i - 1
            col = j - 1
            while row >= 0 and col >= 0:
                if curr[row][col] == 'Q':
                    return False

                row -= 1
                col -= 1

            # Check upper-right diagonal
            row = i - 1
            col = j + 1
            while row >= 0 and col < n:
                if curr[row][col] == 'Q':
                    return False

                row -= 1
                col += 1

            return True
            

        def backtrack(i):
            if i >= n:
                currFormat = ["".join(row) for row in curr[:]]
                res.append(currFormat)
                return
            
            for k in range(n):
                if isValid(i, k, curr):
                    curr[i][k] = 'Q'
                    backtrack(i+1)
                    curr[i][k] = '.'
            
        backtrack(0)

        return res