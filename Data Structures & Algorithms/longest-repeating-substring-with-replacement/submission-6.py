class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        freq = {}

        
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] = freq.get(s[l]) - 1
                l+=1

            maxLength = max(maxLength, r-l+1)

        return maxLength

        