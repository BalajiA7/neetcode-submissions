class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        curr = []
        visited = set()

        def dfs():
            if len(curr) == n:
                print(curr)
                res.append(curr[:])
                return
            
            for i in range(n):
                print(i)
                if nums[i] not in visited:
                    visited.add(nums[i])
                    curr.append(nums[i])
                    dfs()
                    curr.pop()
                    visited.remove(nums[i])
        
        dfs()
        return res
        