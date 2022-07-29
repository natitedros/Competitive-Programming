# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def rec(left, right):
            if left == right:
                return TreeNode(nums[left])
            elif left > right:
                return None
            mid = left + (right-left)//2
            node = TreeNode(nums[mid])
            node.left = rec(left,mid-1)
            node.right = rec(mid+1,right)
            return node
        return rec(0,n-1)