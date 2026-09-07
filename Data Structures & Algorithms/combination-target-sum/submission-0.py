class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)

        def dfs(i, total):
            if i == n:
                if total == target:
                    res.append(curr[:])
                    return
                return
            
            if total == target:
                res.append(curr[:])
                return
            
            if total > target:
                return

            # don't pick
            dfs(i+1, total)
            # pick any number of times
            curr.append(nums[i])
            total+= nums[i]
            dfs(i, total)
            total-= nums[i]
            curr.pop()

        
        dfs(0, 0)
        return res