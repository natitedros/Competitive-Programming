# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isInbound(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n
    
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        visited = set()
        node = head
        row, col = 0, 0
        dx, dy = 0, 1
        while node:
            matrix[row][col] = node.val
            visited.add((row,col))
            node = node.next
            if not self.isInbound(row+dx, col+dy, m, n) or (row+dx, col+dy) in visited:
                dx, dy = dy, -dx
            row += dx
            col += dy
        return matrix
        