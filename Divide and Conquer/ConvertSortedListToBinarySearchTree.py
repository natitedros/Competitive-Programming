# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def rec(start):
            if not start:
                return None
            if not start.next:
                return TreeNode(start.val)
            slow,fast,prev = start,start,start
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            node = TreeNode(slow.val)
            prev.next = None
            node.left = rec(start)
            node.right = rec(slow.next)
            return node
        return rec(head)