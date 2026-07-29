class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {'}': '{', ']': '[', ')': '('}
        stack = []

        for char in s:
            if char in charMap:
                if stack:
                    top = stack.pop()
                    if charMap[char] != top:
                        return False
                else:
                    return False
            else:
                stack.append(char)

        return False if len(stack) else True 