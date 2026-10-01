class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        temp = temperatures
        res = [0] * n
        stack = [] # Montonically decreasing stack

        for i in range(n):
            while stack and temp[i] > stack[-1][1]:
                idx, val = stack.pop()
                res[idx] = i - idx
            stack.append((i, temp[i]))
        
        return res
        