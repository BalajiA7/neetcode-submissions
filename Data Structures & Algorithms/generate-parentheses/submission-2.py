class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def allParenthesis(openCount, closeCount, curr):
            if openCount == 0 and closeCount == 0:
                val = "".join(curr[:])
                res.append(val)
                return
            
            if openCount > 0:
                curr.append("(")
                allParenthesis(openCount-1, closeCount, curr)
                curr.pop()
            
            if openCount < closeCount:
                curr.append(")")
                allParenthesis(openCount, closeCount-1,curr)
                curr.pop()
        
        allParenthesis(n, n, [])
        return res
        