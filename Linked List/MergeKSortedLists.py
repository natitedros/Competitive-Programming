# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        freq = defaultdict(int)
        for node in lists:
            while node:
                freq[node.val] += 1
                node = node.next
        frequency = sorted(freq.items())
        res = ListNode(-1)
        ptr = res
        for val,f in frequency:
            while f:
                ptr.next = ListNode(val)
                ptr = ptr.next
                f -= 1
        return res.next
 