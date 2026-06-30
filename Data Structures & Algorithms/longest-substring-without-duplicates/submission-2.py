class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in subStr:
                subStr.remove(s[l])
                l+=1
            subStr.add(s[r])
            res = max(res, r-l+1)
 
        return res

        