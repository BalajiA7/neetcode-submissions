class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(openCount, closeCount):
            if openCount == 0 and closeCount == 0:
                res.append(''.join(curr[:]))
                return
            
            if openCount:
                curr.append('(')
                dfs(openCount - 1, closeCount)
                curr.pop()
            
            if closeCount > openCount:
                curr.append(')')
                dfs(openCount, closeCount - 1)
                curr.pop()
        
        dfs(n, n)

        return res
