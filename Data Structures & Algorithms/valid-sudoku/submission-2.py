class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        groupMap = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == '.': continue
                if val in rowMap[i] or val in colMap[j] or val in groupMap[(i//3, j//3)]:
                    return False
                rowMap[i].add(val)
                colMap[j].add(val)
                groupMap[(i//3, j//3)].add(val)

        return True                     