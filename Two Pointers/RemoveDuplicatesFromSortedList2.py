# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique = []
        if not head:
            return None
        elif not head.next:
            return head
        prevPtr = head
        ptr = head.next
        while prevPtr:
            if not ptr or ptr.val != prevPtr.val:
                unique.append(prevPtr.val)
            else:
                while ptr and ptr.val == prevPtr.val:
                    ptr = ptr.next
            prevPtr = ptr
            if ptr:
                ptr = ptr.next
        node = head
        prevNode = head
        l = len(unique)
        if not l:
            return None
        for i in range(l):
            node.val = unique[i]
            prevNode = node
            node = node.next
        prevNode.next = None
        return head