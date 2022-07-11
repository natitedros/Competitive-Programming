# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = {}
        def rec(node,lvl):
            if node:
                if lvl not in level:
                    level[lvl] = []
                level[lvl].append(node.val)
                rec(node.right, lvl+1)
                rec(node.left, lvl+1)
        rec(root, 0)
        res = []
        for key in level.keys():
            res.append(level[key][0])
        return res