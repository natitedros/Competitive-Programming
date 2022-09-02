# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, maxVal):
        if not node:
            return 0
        temp = 0
        if node.val >= maxVal:
            temp = 1
        maxVal = max(maxVal, node.val)
        return self.dfs(node.left, maxVal)+self.dfs(node.right, maxVal)+temp
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)