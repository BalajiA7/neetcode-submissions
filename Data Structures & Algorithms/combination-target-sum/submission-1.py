class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        curr = []

        def pickOrNotPick(idx, total):
            if idx == n and total == 0:
                res.append(curr[:])
                return
            
            if idx == n:
                return 

            # pick
            if total-nums[idx] >= 0:
                curr.append(nums[idx])
                pickOrNotPick(idx, total-nums[idx])
                curr.pop()
            # Not pick
            pickOrNotPick(idx+1, total)
        
        pickOrNotPick(0, target)
        return res
