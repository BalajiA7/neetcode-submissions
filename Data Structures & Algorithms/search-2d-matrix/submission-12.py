class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        rowStart, rowEnd = 0, n-1

        while rowStart <= rowEnd:
            row = (rowStart + rowEnd) // 2
            if matrix[row][0] <= target <= matrix[row][m-1]:
                # target lies on the current row
                colStart, colEnd = 0, m-1
                while colStart <= colEnd:
                    col = (colStart + colEnd) // 2
                    if matrix[row][col] == target:
                        return True
                    elif matrix[row][col] > target:
                        colEnd = col - 1
                    else:
                        colStart = col + 1
                return False
            elif matrix[row][0] > target:
                rowEnd = row - 1
            else:
                rowStart = row + 1

        return False
        