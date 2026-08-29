class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.mins = self.mins[:-1]

    def top(self) -> int:
        return self.stack[-1] if self.stack  else  0

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else  0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()