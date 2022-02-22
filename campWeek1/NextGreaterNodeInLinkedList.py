class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        node = head
        i=0
        while node != None:
            res.append(0)
            while stack and stack[-1][0]<node.val:
                res[stack.pop()[1]] = node.val
                
            stack.append([node.val,i])
            node = node.next
            i += 1
        return res