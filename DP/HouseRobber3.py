# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, node, canRob, dp):
            if not node:
                return 0
            if (node, canRob) in dp:
                return dp[(node, canRob)]
            if not canRob:
                dp[(node, canRob)] = self.rec(node.left, not canRob, dp) + self.rec(node.right, not canRob, dp)
            else:
                leftRobbed = self.rec(node.left, not canRob, dp)
                rightRobbed = self.rec(node.right, not canRob, dp)
                leftNotRobbed = self.rec(node.left, canRob, dp)
                rightNotRobbed = self.rec(node.right, canRob, dp)
                dp[(node, canRob)] = max((node.val+leftRobbed+rightRobbed),(leftNotRobbed+rightNotRobbed))
            return dp[(node, canRob)]
        
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.rec(root, True, {})
                