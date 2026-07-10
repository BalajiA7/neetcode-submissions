class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if not val in "+-*/":
                stack.append(int(val))
            else:
                print(val, stack)
                res = 0
                b = stack.pop()
                a = stack.pop()

                if val == '+':
                    res = a+b
                elif val == '*':
                    res = a*b
                elif val == '/':
                    res = int(a/b)
                elif val == '-':
                    res = a-b

                stack.append(res)

        return int(stack[-1])