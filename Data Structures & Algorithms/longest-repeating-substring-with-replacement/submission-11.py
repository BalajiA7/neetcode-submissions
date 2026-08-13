class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        res = 0
         
        maxFreq = 0
        for r in range(0, len(s)):
            # process the current element
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq.get(s[r]))

            #check for window validation
            while (r-l+1) - maxFreq > k:
                #start removing characters from beginning
                # if maxFreq == freq.get(s[l]):
                #     maxFreq -= 1
                freq[s[l]] = freq.get(s[l], 0) - 1
                l+=1

            #window is valid
            res = max(res, r-l+1)
        
        return res
        