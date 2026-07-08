class Solution:
    def isValid(self, s: str) -> bool:
        # l , r = 0,len(s)-1

        # while l < r:
        #     a = s[l]
        #     b = s[r]

        #     if a == '(' and b == ')' or a == '[' and b == ']' or a == '{' and b == '}':
        #         l+=1
        #         r-=1
        #     else:
        #         return False

        # map = {}
        # for char in s:
        #     map[char] = map.get(char, 0) + 1
        
        # for key,value in map.items():
        #     if key == '(' and value != map.get(')', 0) or key == '{' and  value != map.get('}', 0) or key == '[' and value != map.get(']', 0):
        #         return False

        pairs = { ')':'(', ']':'[', '}':'{' }
        stack = []

        for char in s:
            if char in '{[(':
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0
        