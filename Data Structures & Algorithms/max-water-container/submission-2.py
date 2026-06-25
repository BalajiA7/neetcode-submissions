class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_sum = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            # calc current container water
            height = min(heights[i],heights[j])
            width = j - i
            curr_sum = height * width
            max_sum = max(max_sum, curr_sum)
            
            # move ith pointer
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
            # while i < j and heights[i+1] > curr_i:
            #     i+=1
            #     break

            # # move jth pointer
            # while i < j and heights[j-1] > curr_j:
            #     j-=1
            #     break
            # i+=1
            # j-=1

            print(i,j)

        return max_sum