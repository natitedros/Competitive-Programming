# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        size = length//k
        added = length%k
        node = head
        prev = head
        count = 0
        res = []
        stop = head
        while node:
            if count == size:
                if added:
                    added -= 1
                    prev = node
                    node = node.next
                prev.next = None
                res.append(stop)
                stop = node
                count = 0
            else:
                count += 1
                prev = node
                node = node.next
        if stop:
            res.append(stop)
        while length < k:
            res.append(None)
            length += 1
        return res