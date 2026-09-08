class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(curr[:])
                return

            # pick
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            # not pick
            dfs(i+1)

        dfs(0)
        return [list(x) for x in set(tuple(val) for val in res)]
