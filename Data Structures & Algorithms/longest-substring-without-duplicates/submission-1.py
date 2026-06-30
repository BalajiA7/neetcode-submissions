class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(0, len(s)):
            subStr = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] in subStr:
                    subStr = set()
                    length = 0
                subStr.add(s[j])
                length +=1
                res = max(res, length)

        return res

        