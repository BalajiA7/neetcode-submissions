class Solution:
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        n = len(s)

        def dfs(i):
            if i >= n:
                res.append(curr[:])
                return

            for idx in range(i, n):
                if self.isPali(s, i, idx):
                    curr.append(s[i: idx+1])
                    dfs(idx+1)
                    curr.pop()
        
        dfs(0)
        return res
