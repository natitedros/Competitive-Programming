"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}
        def rec(original):
            if not original:
                return None
            if original in visited:
                return visited[original]
            copy = Node(original.val)
            visited[original] = copy
            copy.next = rec(original.next)
            copy.random = rec(original.random)
            return copy
        return rec(head)