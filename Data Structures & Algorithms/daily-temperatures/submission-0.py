class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * (len(temperatures))

        for i in range(len(temperatures)):
            nofDays = 0
            for j in range(i+1, len(temperatures)):
                nofDays+=1
                if temperatures[j] > temperatures[i]:
                    res[i] = nofDays
                    break
        return res
        