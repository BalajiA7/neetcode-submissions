class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        gridMap = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue
                
                if val in rowMap[i] or val in colMap[j] or val in gridMap[(i//3, j//3)]:
                    return False
                
                rowMap[i].append(val)
                colMap[j].append(val)
                gridMap[(i//3, j//3)].append(val)
        
        return True
