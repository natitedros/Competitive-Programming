class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head
        counter = 0
        while front.next:
            front = front.next
            if counter >= n:
                back = back.next
            counter += 1
        if back != front and counter >= n:
            back.next = back.next.next
        elif counter < n:
            head = head.next
        else:
            head = None
        return head