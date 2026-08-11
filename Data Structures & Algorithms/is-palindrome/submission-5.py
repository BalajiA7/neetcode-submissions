class Solution:
    def isAlphaNumeric(self, char):
        val = ord(char)
        return (ord('A') <= val <= ord('Z')) or (ord('a') <= val <= ord('z')) or (ord('0') <= val <= ord('9'))
        
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1

        while l < r:
            a = s[l].lower()
            b = s[r].lower()
            if not self.isAlphaNumeric(a):
                l+=1
            elif not self.isAlphaNumeric(b):
                r-=1
            else:
                if a != b:
                    return False
                l+=1
                r-=1
        
        return True

        