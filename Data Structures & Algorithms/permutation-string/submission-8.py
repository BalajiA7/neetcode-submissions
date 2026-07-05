class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "".join(sorted(s1))
        # s2 = "".join(sorted(s2))

        l = 0

        for r in range(len(s2)):

            if r-l+1 == len(s1):
                currStr = s2[l:r+1]
                print(l, r, currStr)
                if "".join(sorted(currStr)) == "".join(sorted(s1)):
                    return True
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


        