class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count = {}
        s2Count = {}

        # calculate s1 Freq Count
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        # calculate s2 Freq Count till s1 Len
        for i in range(len(s1)):
             s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1
        
        need = len(s1Count)
        have = 0

        # calculate have count
        for char,value in s1Count.items():
            if s2Count.get(char,0) >= value:
                have+=1
        print("stage 1", have, need, s1Count, s2Count)
        if need == have: return True

        l = 0
        r = len(s1)
        while r < len(s2):
            # process the current element
            c = s2[r]
            s2Count[c] = s2Count.get(c, 0) + 1
            if c in s1Count and s2Count[c] == s1Count[c]:
                have+=1
            print("stage 2", have, need, s1Count, s2Count)

            # remove invalid elements from the window
            # while (r-l+1) > len(s1):
            
            if s2[l] in s1Count and s2Count[s2[l]] == s1Count[s2[l]]:
                have-=1
            s2Count[s2[l]] -=1
            l+=1
            
            # window is valid
            if have == need:
                return True

            r+=1
        
        return False





        