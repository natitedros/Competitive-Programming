"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        temp = []
        q = deque()
        q.append((root,0))
        prevLvl = 0
        while q:
            node,lvl = q.popleft()
            if lvl != prevLvl:
                res.append(temp)
                temp = []
                prevLvl = lvl
            temp.append(node.val)
            for child in node.children:
                q.append((child,lvl+1))
        if temp:
            res.append(temp)
        return res