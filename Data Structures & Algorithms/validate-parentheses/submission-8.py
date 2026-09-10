class Solution:
    def isValid(self, s: str) -> bool:
        match = {'[': ']', '{': '}', '(': ')'}

        stack = []
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if stack and match[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
                


        