class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # Intialize & count Freq of t
        resLen = float('inf')
        resI, resJ = 0, 0

        tFreq = {}
        sFreq = {}

        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1

        l = 0
        for r in range(len(s)):
            # Increase the window
            c = s[r]
            sFreq[c] = sFreq.get(c, 0) + 1

            # if both are equal update the result with min index
            while all(sFreq.get(c,0) >= tFreq[c] for c in t):
                if r - l + 1 < resLen:  # ← found a smaller window
                    resLen = r - l + 1
                    resI = l
                    resJ = r

                # Decrease the window
                sFreq[s[l]] -= 1
                if sFreq[s[l]] == 0:
                    del sFreq[s[l]]

                l+=1
                        
        if resLen == float('inf'):
            return ""

        return s[resI:resJ+1]




        