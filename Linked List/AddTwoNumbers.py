# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sm = l1.val+l2.val
        l1 = l1.next
        l2 = l2.next
        l3 = ListNode(sm%10)
        ptr3 = l3
        carry = sm//10
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2: 
                temp += l2.val
                l2 = l2.next
            temp += carry
            carry = temp // 10
            node = ListNode(temp%10)
            ptr3.next = node
            ptr3 = ptr3.next
        if carry:
            node = ListNode(carry)
            ptr3.next = node
        return l3