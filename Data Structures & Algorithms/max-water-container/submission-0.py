class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_sum = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                curr_sum = height * width
                max_sum = max(max_sum, curr_sum)

        return max_sum