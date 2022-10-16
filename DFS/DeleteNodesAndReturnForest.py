# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        to_delete = set(to_delete)
        def finder(node):
            if not node:
                return None
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    forest.append(node.left)
                finder(node.left)
                if node.right and node.right.val not in to_delete:
                    forest.append(node.right)
                finder(node.right)
                return None
            node.left = finder(node.left)
            node.right = finder(node.right)
            return node
        if finder(root):
            forest.append(root)
        return forest
            