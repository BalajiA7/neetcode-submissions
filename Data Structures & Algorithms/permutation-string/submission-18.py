class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for c in s1:
            s1Freq[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(0, len(s2)):
            # Add to window
            s2Freq[ord(s2[r]) - ord('a')] +=1
            # check window length
            if (r-l+1) == len(s1):
                if s1Freq == s2Freq:
                    return True
                #Remove from beginning
                s2Freq[ord(s2[l]) - ord('a')] -=1
                l+=1
        
        return False
        