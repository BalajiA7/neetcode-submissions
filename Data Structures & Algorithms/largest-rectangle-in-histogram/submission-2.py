class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = []

        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                left = stack[-1][0] if stack else -1
                width = i - left - 1
                maxArea = max(maxArea, height * width)

            stack.append((i,h))
        
        while stack:
            index, height = stack.pop()
            left = stack[-1][0] if stack else - 1
            width = n - left - 1
            maxArea = max(maxArea, height * width)
        
        return maxArea

        