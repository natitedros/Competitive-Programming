# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(0,head)
        d = {0:fake}
        ptr = head
        prefix = 0
        while ptr:
            prefix += ptr.val
            d[prefix] = ptr
            ptr = ptr.next
        ptr = fake
        prefix = 0
        while ptr:
            prefix += ptr.val
            ptr.next = d[prefix].next
            ptr = ptr.next
        return fake.next            