class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        visited = [False] * len(nums)

        def dfs(curr, visited):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(0, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    curr.append(nums[i])
                    dfs(curr, visited)
                    visited[i] = False
                    curr.pop()
        
        dfs(curr, visited)
        return res

        