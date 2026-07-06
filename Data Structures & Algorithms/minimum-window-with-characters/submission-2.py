class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # Intialize & count Freq of t
        resLen = float('inf')
        resI, resJ = 0, 0

        tFreq = [0] * 52
        for c in t:
            if c.isupper():
                tFreq[ord(c)- ord('A')] +=1
            else:
                tFreq[26 + ord(c)- ord('a')] +=1

        for i in range(len(s)):
            sFreq = [0] * 52
            for j in range(i, len(s)):
                if s[j].isupper():
                    sFreq[ord(s[j])- ord('A')] +=1
                else:
                    sFreq[26 + ord(s[j])- ord('a')] +=1

                # compare sFreq and sFreq are equal
                isEqual = all(sFreq[i] >= tFreq[i] for i in range(52))
                # if both are equal update the result with min index
                if isEqual:
                    if j - i + 1 < resLen:  # ← found a smaller window
                        resLen = j - i + 1
                        resI = i
                        resJ = j

        if resLen == float('inf'):
            return ""

        return s[resI:resJ+1]




        