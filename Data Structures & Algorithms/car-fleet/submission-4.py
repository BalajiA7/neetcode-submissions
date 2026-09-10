class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort()
        
        time = []
        for p,s in pairs:
            destination = (target-p) / s
            time.append(destination)
        
        stack = [] #mono decreasing
        
        for i in range(len(time)-1, -1, -1):
            if not stack:
                stack.append(time[i])
            else:
                if time[i] > stack[-1]:
                    stack.append(time[i])

        return len(stack) 

        