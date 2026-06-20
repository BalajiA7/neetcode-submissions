class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board)):
            row_set = set()
            col_set = set()
            for j in range(0, len(board)):
                # Row -> [i][j]
                # Col -> [j][i]
                row_value = board[i][j]
                col_value = board[j][i]
                if row_value != ".":
                    if row_value in row_set:
                        return False
                    row_set.add(row_value)

                if col_value != ".":
                    if col_value in col_set:
                        return False
                    col_set.add(col_value)
                print(row_set, col_set)

        for i in range(0, len(board),3):
            for j in range(0, len(board),3):
                group_set = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        value = board[k][l]
                        if value != ".":
                            if value in group_set:
                                return False
                            group_set.add(value)
        
        return True





