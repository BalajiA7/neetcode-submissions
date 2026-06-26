class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        
        curr_max = 0
        for i in range(1, len(height)):
            curr_max = max(curr_max, height[i-1])
            left_max[i] = curr_max

        curr_max = 0
        for i in range(len(height)-2,-1,-1):
            curr_max = max(curr_max, height[i+1])
            right_max[i] = curr_max
        
        print(left_max, right_max)

        for i in range(0, len(height)):
            curr_height = height[i]
            left_maxvalue, right_maxValue = left_max[i],right_max[i]
            curr_water = min(left_maxvalue,right_maxValue) - curr_height
            if curr_water > 0:
                trapped_water += curr_water
            
        return trapped_water
        