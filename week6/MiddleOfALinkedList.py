class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodePtr = head
        counter = 0
        arr = []
        while nodePtr:
            counter += 1
            arr.append(nodePtr)
            nodePtr = nodePtr.next
        return arr[math.floor(counter/2)]
        