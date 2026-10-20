class Solution:
    def nearestSmallestEleLeft(self, heights):
        n = len(heights)
        res = [0] * n
        stack = []
        
        for i in range(n):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            res[i] = stack[-1][0] if stack else -1
            stack.append((i, heights[i]))

        return res

    def nearestSmallestEleRight(self, heights):
        n = len(heights)
        res = [0] * n
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            res[i] = stack[-1][0] if stack else n
            stack.append((i, heights[i]))
            
        return res


    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = heights[0]
        left = self.nearestSmallestEleLeft(heights)
        right = self.nearestSmallestEleRight(heights)

        for i in range(n):
            maxArea = max(maxArea, heights[i] * (right[i] - left[i] - 1))
        
        return maxArea






