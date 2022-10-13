# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = 0
        res = 0
        def inorder(node):
            nonlocal pos,res
            if not node or pos > k:
                return
            inorder(node.left)
            pos += 1
            if pos == k:
                res = node.val
                return
            inorder(node.right)
        inorder(root)
        return res
            