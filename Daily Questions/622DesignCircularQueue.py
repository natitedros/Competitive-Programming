class MyCircularQueue:

    def __init__(self, k: int):
        self.stack = [0]*k
        self.front = 0
        self.back = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.back = (self.back+1)%len(self.stack)
            self.stack[self.back] = value
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front+1)%len(self.stack)
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.stack[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.stack[self.back]

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == len(self.stack) else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()