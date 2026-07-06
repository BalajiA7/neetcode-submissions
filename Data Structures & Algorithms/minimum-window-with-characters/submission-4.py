class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # Intialize & count Freq of t
        resLen = float('inf')
        resI, resJ = 0, 0

        tFreq = [0] * 52
        sFreq = [0] * 52

        for c in t:
            if c.isupper():
                tFreq[ord(c)- ord('A')] +=1
            else:
                tFreq[26 + ord(c)- ord('a')] +=1

        l = 0
        for r in range(len(s)):
            # Increase the window
            if s[r].isupper():
                sFreq[ord(s[r])- ord('A')] +=1
            else:
                sFreq[26 + ord(s[r])- ord('a')] +=1

            # if both are equal update the result with min index
            while all(sFreq[i] >= tFreq[i] for i in range(52)):
                if r - l + 1 < resLen:  # ← found a smaller window
                    resLen = r - l + 1
                    resI = l
                    resJ = r

                # Decrease the window
                if s[l].isupper():
                    sFreq[ord(s[l])- ord('A')] -=1
                else:
                    sFreq[26 + ord(s[l])- ord('a')] -=1
                l+=1
                        
        if resLen == float('inf'):
            return ""

        return s[resI:resJ+1]




        