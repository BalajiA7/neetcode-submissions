class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Map, s2Map = {}, {}
        # s1 freq
        for c in s1:
            s1Map[c] = s1Map.get(c,0) + 1
        
        l = 0
        need = len(s1Map)
        have = 0
        for r in range(len(s2)):
            rightChar = s2[r]
            #process the current element
            s2Map[rightChar] = s2Map.get(rightChar, 0) + 1
            if rightChar in s1Map and s2Map[rightChar] == s1Map[rightChar]:
                have+=1
            # Fixed window
            if (r-l+1) == len(s1):
                if have == need: return True
                leftchar = s2[l]
                if leftchar in s1Map and s2Map[leftchar] == s1Map[leftchar]:
                    have-=1
                s2Map[leftchar] -=1
                l+=1

        return False

        