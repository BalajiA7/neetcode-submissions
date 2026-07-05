class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "".join(sorted(s1))
        # s2 = "".join(sorted(s2))

        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        l = 0
        count2 = {}
        for r in range(len(s2)):
            c = s2[r]
            count2[c] = 1 + count2.get(c, 0)

            if (r-l+1) == len(s1):
                if count1 == count2:
                    return True
                count2[s2[l]] -=1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l +=1
        return False

        # for i in range(0,len(s2)):
        #     currStr = ""
        #     j = i

        #     while j < (i+len(s1)) and j < len(s2):
        #         currStr+= s2[j]
        #         j+=1
                
        #     print(s1,s2,i,j,currStr)
        #     if "".join(sorted(currStr)) == "".join(sorted(s1)):
        #         return True

        # return False    


        