class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["*", "+", "-", "/"]
        stack = []
        
        for token in tokens:
            if token in operator:
                b = stack.pop()
                a = stack.pop()
                val = 0
                if token == "+":
                    val = a+b
                elif token == "*":
                    val = a*b
                elif token == "-":
                    val = a-b
                else:
                    val = int(a/b)
                stack.append(val)
            else:
                stack.append(int(token))
        
        return stack[-1]
