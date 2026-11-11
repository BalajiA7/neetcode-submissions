class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        curr = []
        candidates.sort()

        def combinationSum(idx, target):
            if target == 0:
                res.append(curr[:])
                return
            
            if idx >= n:
                return
            
            # pick case
            if target-candidates[idx] >= 0:
                curr.append(candidates[idx])
                combinationSum(idx+1, target-candidates[idx])
                curr.pop()

            # not pick case
            i = idx
            while i+1 < n and candidates[i] == candidates[i+1]:
                i+=1
            combinationSum(i+1, target)
        
        combinationSum(0, target)
        return res


        