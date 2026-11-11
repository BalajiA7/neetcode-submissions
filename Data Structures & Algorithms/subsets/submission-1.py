class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        curr = []

        def subset(idx):
            if idx == n:
                res.append(curr[:])
                return
            
            # Pick the index
            curr.append(nums[idx])
            subset(idx+1)
            curr.pop()

            # not pick the index
            subset(idx+1)
        
        subset(0)
        return res
        