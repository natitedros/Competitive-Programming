# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(node):
            if node and node.val > val:
                return rec(node.left)
            elif node and node.val < val:
                return rec(node.right)
            return node
        return rec(root)