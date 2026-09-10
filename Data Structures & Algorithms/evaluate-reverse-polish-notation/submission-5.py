class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+", "-", "*", "/"]
        
        stack = []
        for c in tokens:
            if c in operator:
                b = stack.pop()
                a = stack.pop()
                res = 0
                if c == "+":
                    res = b+a
                elif c == "*":
                    res = b*a
                elif c == "-":
                    res = a-b
                else:
                    res = int(a/b) 
                stack.append(res)
            else:
                stack.append(int(c))

        return stack[-1]
