class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        curr = []
        visited = set()

        def dfs():
            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    curr.append(nums[i])
                    dfs()
                    curr.pop()
                    visited.remove(i)
        
        dfs()
        return res
        