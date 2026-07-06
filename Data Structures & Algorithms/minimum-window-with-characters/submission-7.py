class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # Intialize & count Freq of t
        resLen = float('infinity')
        resI, resJ = 0, 0

        tFreq = {}
        sFreq = {}

        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1

        have,need = 0, len(tFreq)
        l = 0
        for r in range(len(s)):
            # Increase the window
            c = s[r]
            sFreq[c] = sFreq.get(c, 0) + 1

            if c in tFreq and tFreq[c] == sFreq[c]:
                have+=1

            # if both are equal update the result with min index
            while have == need:
                if r - l + 1 < resLen:  # ← found a smaller window
                    resLen = r - l + 1
                    resI = l
                    resJ = r

                # Decrease the window
                sFreq[s[l]] -= 1

                if s[l] in tFreq and sFreq[s[l]] < tFreq[s[l]]:
                    have-=1
        
                l+=1
                        
        if resLen == float('inf'):
            return ""

        return s[resI:resJ+1]




        