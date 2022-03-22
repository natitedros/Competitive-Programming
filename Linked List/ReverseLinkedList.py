class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        nodePtr = head
        while nodePtr:
            stack.append(nodePtr.val)
            nodePtr = nodePtr.next
        nodePtr = head
        while stack != []:
            temp = stack.pop()
            nodePtr.val = temp
            nodePtr = nodePtr.next
        return head