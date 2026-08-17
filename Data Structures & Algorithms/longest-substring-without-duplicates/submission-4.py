class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqMap = {}
        l, res = 0,0

        for r in range(0, len(s)):
            # check for invalid
            while l < len(s) and s[r] in freqMap:
                freqMap[s[l]] = freqMap[s[l]] - 1
                if freqMap[s[l]] == 0:
                    del freqMap[s[l]]
                l+=1

            # window is valid
            freqMap[s[r]] = freqMap.get(s[r],0) + 1
            res = max(res, r-l+1)
        
        return res

        