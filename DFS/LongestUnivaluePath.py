# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxLen = 0
        def dfs(node,val):
            nonlocal maxLen
            if not node:
                return 0
            if node.val != val:
                left = dfs(node.left,node.val)
                right = dfs(node.right,node.val)
                maxLen = max(maxLen,left+right,max(left,right))
                return 0
            else:
                left = dfs(node.left,val)
                right = dfs(node.right,val)
                maxLen = max(maxLen,left+right)
                return 1 + max(left,right)
        dfs(root,1001)
        return maxLen