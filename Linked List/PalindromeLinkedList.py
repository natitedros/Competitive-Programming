# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        temp = count//2
        prev,node,later = None,head,head.next
        while temp > 0:
            node.next = prev
            prev = node
            node = later
            later = later.next
            temp -= 1
        if count%2:
            node = later
        while prev or node:
            if node.val != prev.val:
                return False
            prev = prev.next
            node = node.next
        return True