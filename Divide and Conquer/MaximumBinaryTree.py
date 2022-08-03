# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(left,right):
            if left > right:
                return None
            elif left == right:
                return TreeNode(nums[left])
            maxInd = left
            for i in range(left,right+1):
                if nums[i]>nums[maxInd]:
                    maxInd = i
            node = TreeNode(nums[maxInd])
            node.left = rec(left,maxInd-1)
            node.right = rec(maxInd+1,right)
            return node
        return rec(0,len(nums)-1)