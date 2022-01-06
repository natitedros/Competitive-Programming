class MyCircularDeque:

    def __init__(self, k: int):
        self.front = 1
        self.rear = 0
        self.counter = 0
        self.maxSize = k
        self.que = [0]*k

    def insertFront(self, value: int) -> bool:
        if self.counter == self.maxSize:
            return False
        else:
            self.front = (self.front-1) % self.maxSize
            self.que[self.front] = value
            self.counter += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.counter == self.maxSize:
            return False
        else:
            self.rear = (self.rear+1) % self.maxSize
            self.que[self.rear] = value
            self.counter += 1
            return True

    def deleteFront(self) -> bool:
        if self.counter == 0:
            return False
        else:
            self.front = (self.front+1) % self.maxSize
            self.counter -= 1
            return True

    def deleteLast(self) -> bool:
        if self.counter == 0:
            return False
        else:
            self.rear = (self.rear-1) % self.maxSize
            self.counter -= 1
            return True

    def getFront(self) -> int:
        if self.counter == 0:
            return -1
        else:
            return self.que[self.front]

    def getRear(self) -> int:
        if self.counter == 0:
            return -1
        else:
            return self.que[self.rear]

    def isEmpty(self) -> bool:
        if self.counter == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.counter == self.maxSize:
            return True
        return False