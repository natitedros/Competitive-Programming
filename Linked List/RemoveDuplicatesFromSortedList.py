class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        front = head
        if head.next:
            back = head
        while front:
            back = front
            front = front.next
            while front and back.val == front.val:
                back.next = front.next
                front = front.next
        return head