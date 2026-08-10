class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        res = 0

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        
        for i in range(len(height)):
            minHeight = min(leftMax[i], rightMax[i]) 
            if minHeight > height[i]:
                res += minHeight - height[i]
        
        return res

        