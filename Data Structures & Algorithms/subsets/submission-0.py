class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)

        def dfs(i):
            if i == n:
                res.append(curr[:])
                return
            # Not Pick 
            dfs(i+1)
            # Pick
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
        
        dfs(0)
        return res
        