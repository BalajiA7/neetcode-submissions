class Solution:
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dfs(idx):
            if idx >= len(s):
                res.append(curr[:])
                return
            
            for i in range(idx, len(s)):
                if self.isPalindrome(s, idx, i):
                    curr.append(s[idx: i+1])
                    dfs(i+1)
                    curr.pop()
        
        dfs(0)
        return res

                                             
        