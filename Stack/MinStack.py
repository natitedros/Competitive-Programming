class MinStack:

    def __init__(self):
        self.stack = []
        self.minStk = [inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStk.append(min(self.minStk[-1],val))

    def pop(self) -> None:
        self.minStk.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()