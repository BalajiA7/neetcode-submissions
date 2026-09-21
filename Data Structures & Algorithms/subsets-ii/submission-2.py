class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def generateAllSubSet(idx):
            if idx >= len(nums):
                res.append(curr[:])
                return

            # not pick idx
            j = idx + 1
            while j < len(nums) and nums[j-1] == nums[j]:
                j+=1

            generateAllSubSet(j)

            # pick idx
            curr.append(nums[idx])
            generateAllSubSet(idx+1)
            curr.pop()
        
        generateAllSubSet(0)
        return res

        