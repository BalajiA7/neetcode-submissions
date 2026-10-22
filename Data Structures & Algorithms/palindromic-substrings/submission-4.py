class Solution:
    def isSubStr(self,s):
        r = len(s)-1
        l = 0

        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            # odd case
            l = i
            r = i

            while l>=0 and r < n:
                if s[l] != s[r]:
                    break
                count += 1
                l-=1
                r+=1
                
            # even case
            l = i-1
            r = i

            while l>=0 and r < n:
                if s[l] != s[r]:
                    break
                count += 1
                l-=1
                r+=1            
    
        return count
