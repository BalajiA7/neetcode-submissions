class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        for i in range(0, len(height)):
            curr_height = height[i]

            left_max, right_max = 0,0
            for j in range(0, i):
                left_max = max(left_max, height[j])
            
            for k in range(i+1, len(height)):
                right_max = max(right_max, height[k])
            
            curr_water = min(left_max,right_max) - curr_height
            if curr_water > 0:
                trapped_water += curr_water
            
        return trapped_water
        