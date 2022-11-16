# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        reverseLimit = length - (length % k)
        group = 0
        start = dummy
        end = start.next
        prev = start
        node = head
        while node:
            group += 1
            if group > reverseLimit:
                break
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            if group%k == 0:
                start.next = prev
                end.next = node
                start = end
                end = start.next
        return dummy.next
