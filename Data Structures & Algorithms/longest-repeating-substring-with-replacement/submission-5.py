class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0

        for i in range(0, len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = 1 + freq.get(s[j], 0)
                windowsLen = j-i+1
                maxElementLength = max(freq.values())
                currLength = windowsLen - maxElementLength
                if currLength <= k:
                    maxLength = max(maxLength, j-i+1)

        return maxLength

        