class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq = {}
        currMax = 0
        
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            currMax = max(currMax, freq[s[r]])

            while (r-l+1) - currMax > k:
                freq[s[l]] = freq.get(s[l]) - 1
                l+=1

            result = max(result, r-l+1)

        return result

        