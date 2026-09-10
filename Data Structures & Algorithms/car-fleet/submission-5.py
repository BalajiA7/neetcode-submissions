class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort()

        stack = [] #mono Increasing        
        for p, s in reversed(pairs):
            timeTaken = (target-p) / s
            if not stack or timeTaken > stack[-1]:
                stack.append(timeTaken)
                
        return len(stack) 

        