# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def rec(start,end):
            if start > end:
                return [None]
            trees = []
            for root in range(start,end+1):
                for left in rec(start,root-1):
                    for right in rec(root+1,end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees
        return rec(1,n)
            