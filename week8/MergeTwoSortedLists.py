class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            head = list2
            list2 = list2.next
        elif list2 == None:
            head = list1
            list1 = list1.next
        elif list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        node = head
        while list1 or list2:
            if list1 == None and list2 != None:
                node.next = list2
                node = node.next
                list2 = list2.next
            elif list2 == None and list1 != None:
                node.next = list1
                node = node.next
                list1 = list1.next
            elif list1.val < list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
            node.next = None
        return head