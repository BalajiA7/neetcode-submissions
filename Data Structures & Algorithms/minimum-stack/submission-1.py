class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else: 
            self.minStack.append(min(self.minStack[-1],val))


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # minValue = float("infinity")
        # for val in self.stack:
        #     minValue = min(minValue, val)
        # return minValue
        return self.minStack[-1]

        
