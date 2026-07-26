class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        n = len(s)
        map1, map2 = {}, {}

        for char in t:
            map1[char] = map1.get(char, 0) + 1
        
        have, need = 0, len(map1)
        l,r = 0,0
        minI, minJ, minLength = 0,0, float('inf') 

        while r < n:
            # valid window
            if s[r] in map1:
                map2[s[r]] = map2.get(s[r], 0) + 1
                if map1[s[r]] == map2[s[r]]:
                    have+=1
            
            # have == need
            while have == need:
                # calculate curr length
                if (r-l+1) < minLength:
                    minLength = r-l+1
                    minI = l
                    minJ = r

                # remove character from start and update have
                if s[l] in map1:
                    if map1[s[l]] == map2[s[l]]:
                        have-=1
                    map2[s[l]] -=1
                l+=1
                
            r+=1
        
        return s[minI:minJ+1] if minLength != float('inf') else ""
                

       




        