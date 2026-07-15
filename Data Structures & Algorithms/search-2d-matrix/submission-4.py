class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) -1
        
        while l<=r:
            mid = l + (r-l) // 2
            n = len(matrix[mid]) -1
            print("Outer Midd", l,r,mid)
            if target >= matrix[mid][0] and target <= matrix[mid][n]:
                print("Inner", l, r)
                innerL = 0
                innerR = n
                while innerL <= innerR:
                    m = innerL + (innerR - innerL) // 2
                    if matrix[mid][m] > target:
                        innerR = m - 1
                    elif matrix[mid][m] < target:
                        innerL = m + 1
                    else:
                        return True
                return False
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid -1
        
        return False

        # for i in range(len(matrix)):
        #     l = 0
        #     r = len(matrix[i]) -1
        #     while l<=r:
        #         mid = l + (r-l) // 2
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] > target:
        #             r = mid -1
        #         else:
        #             l = mid + 1
        # return False
        