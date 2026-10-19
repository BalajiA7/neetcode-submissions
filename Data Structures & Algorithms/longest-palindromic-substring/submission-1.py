class Solution:
    def palindrome(self, s):
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return False        
        return True

    def longestPalindrome(self, s: str) -> str:
        resLength = 0
        result = ""
        n  = len(s)
        
        # odd case
        for i in range(n):
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                currLength = r-l+1
                if currLength > resLength:
                    resLength = currLength
                    result = s[l:r+1]
                l-=1
                r+=1
        
        # Even Cases
        for i in range(n):
            l, r = i, i+1

            while l >= 0 and r < n and s[l] == s[r]:
                currLength = r-l+1
                if currLength > resLength:
                    resLength = currLength
                    result = s[l:r+1]
                l-=1
                r+=1
        
        return result
