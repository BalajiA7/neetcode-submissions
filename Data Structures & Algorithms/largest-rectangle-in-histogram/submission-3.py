class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for i,ele in enumerate(heights):
            while stack and ele < stack[-1][1]:
                stk_idx, stk_ele = stack.pop()
                leftIdx = stack[-1][0] if stack else -1
                maxArea = max(maxArea, stk_ele * (i-leftIdx-1))
            stack.append((i,ele))
        
        print("Stack", stack, maxArea)

        while stack:
            stk_idx, stk_ele = stack.pop()
            leftIdx = stack[-1][0] if stack else -1
            maxArea = max(maxArea, stk_ele * (n-leftIdx-1))

        return maxArea