class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cap = 0
        self.head, self.tail = ListNode([-1,-1]), ListNode([-1,-1])
        self.head.next = self.tail
        self.tail.prev = self.head
        self.Dict = {}

    def get(self, key: int) -> int:
        
        if key not in self.Dict:
            return -1
        temp = self.Dict[key]
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = self.tail.prev
        self.tail.prev.next = temp
        self.tail.prev = temp
        temp.next = self.tail
        return temp.val[1]

    def put(self, key: int, value: int) -> None:
        temp = ListNode([key,value])
        if key in self.Dict:
            temp = self.Dict[key]
            temp.val[1] = value
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.cap -= 1
        elif self.cap >= self.capacity:
            del self.Dict[self.head.next.val[0]]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.cap -= 1
        self.tail.prev.next = temp
        temp.prev = self.tail.prev
        self.tail.prev = temp
        temp.next = self.tail
        self.cap += 1
        self.Dict[key] = temp
        
            
            
            
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)