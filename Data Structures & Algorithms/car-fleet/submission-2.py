class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort()
        stack = []

        for pair in reversed(pairs):
            p,s = pair
            timeTaken = (target - p)  / s

            if not stack or not timeTaken <= stack[-1]:
                stack.append(timeTaken)

        return len(stack)
        