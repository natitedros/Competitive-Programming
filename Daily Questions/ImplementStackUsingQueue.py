class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

    def pop(self) -> int:
        if not self.q1 and self.q2:
            self.q1, self.q2 = self.q2, self.q1
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
        return self.q1.popleft()
        
    def top(self) -> int:
        if not self.q1 and self.q2:
            self.q1, self.q2 = self.q2, self.q1
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1 and not self.q2
