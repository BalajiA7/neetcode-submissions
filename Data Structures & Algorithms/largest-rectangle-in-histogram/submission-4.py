class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        total = 0

        for ind,val in enumerate(heights):
            while stack and val < stack[-1][1]:
                topInd, topVal = stack.pop()
                leftIdx = stack[-1][0] if stack else -1
                total = max(total, topVal * (ind - leftIdx - 1))
            stack.append((ind,val))

        while stack:
            topInd, topVal = stack.pop()
            rightIdx = len(heights)
            leftIdx = stack[-1][0] if stack else -1
            total = max(total, topVal * (rightIdx - leftIdx - 1))
        
        return total
            
        