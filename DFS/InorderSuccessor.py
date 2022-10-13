# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, t, successor=inf):
        if not node:
            return successor
        if node.val > t:
            return self.solve(node.left,t,min(successor,node.val))
        else:
            return self.solve(node.right,t,successor)
        