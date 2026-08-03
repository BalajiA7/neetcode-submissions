class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for ind, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                topVal, topInd = stack.pop()
                res[topInd] = ind - topInd
            stack.append((val, ind))
        
        return res
        
        