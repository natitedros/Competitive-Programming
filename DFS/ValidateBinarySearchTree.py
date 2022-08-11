# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, inf, -1*inf]
            left = dfs(node.left)
            right = dfs(node.right)
            if not left[0] or not right[0]:
                return [False,inf,-1*inf]
            elif (left[2] and left[2]>=node.val) or (right[1] and right[1]<=node.val):
                return [False,inf,-1*inf]
            return [True,min(node.val,left[1]),max(node.val,right[2])]
        res = dfs(root)
        return res[0]