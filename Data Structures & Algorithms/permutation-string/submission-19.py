class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for c in s1:
            s1Freq[ord(c) - ord('a')] += 1
        
        need, have  = 0, 0
        for v in s1Freq:
            if v > 0:
                need+=1

        l = 0
        for r in range(0, len(s2)):
            # Add to window
            idx = ord(s2[r]) - ord('a')
            s2Freq[idx] +=1
            if s1Freq[idx] == s2Freq[idx]:
                have+=1

            # check window length
            if (r-l+1) == len(s1):
                if have == need:
                    return True
                #Remove from beginning
                idx = ord(s2[l]) - ord('a')
                if s1Freq[idx] == s2Freq[idx]:
                    have-=1
                s2Freq[idx] -=1
                l+=1
        
        return False
        