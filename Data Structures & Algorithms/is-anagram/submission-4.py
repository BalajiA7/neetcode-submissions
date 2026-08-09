class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # freq = [0] * 26
        # for c in s:
        #     freq[ord(c)-ord('a')]+=1
                
        # for c in t:
        #     freq[ord(c)-ord('a')]-=1
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1
        
        for count in freq.values():
            if count != 0:
                return False
        
        return True
        