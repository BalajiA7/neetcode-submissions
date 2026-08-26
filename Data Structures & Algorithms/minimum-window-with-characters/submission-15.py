class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
            
        mapt = {}
        for c in t:
            mapt[c] = mapt.get(c, 0) + 1
        
        l = 0
        maps = {}
        length = float("infinity")
        minI, minR = 0, 0
        need = len(mapt)
        have = 0
        
        for r in range(len(s)):
            # process the current character
            c = s[r]
            maps[c] = maps.get(c, 0) + 1
            if mapt.get(c,0) == maps[c]:
                have+=1

            while have == need:
                # current window is valid calculate the length
                if r-l+1 <= length:
                    length = r-l+1
                    minI = l
                    minR = r
                # remove the characater from beginning
                c1 = s[l]
                if mapt.get(c1, 0) == maps[c1]:
                    have-=1
                maps[c1] -=1
                l+=1

        if length == float("infinity"):
            return ""

        return s[minI:minR+1]

            

        