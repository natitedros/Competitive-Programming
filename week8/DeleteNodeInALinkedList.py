class Solution:
    def deleteNode(self, node):
        prevPtr = node
        while node.next:
            node.val = node.next.val
            prevPtr = node
            node = node.next
        prevPtr.next = None