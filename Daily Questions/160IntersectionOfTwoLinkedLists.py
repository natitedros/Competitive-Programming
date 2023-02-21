# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        freq = defaultdict(int)
        while headA:
            freq[headA] += 1
            headA = headA.next
        while headB:
            freq[headB] += 1
            headB = headB.next
        for key in freq.keys():
            if freq[key] == 2:
                return key
        return None