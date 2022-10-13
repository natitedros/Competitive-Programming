# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def successor(node):
            if not node.right:
                return node
            return successor(node.right)
        
        def find(node):
            if not node:
                return None
            if node.val < key:
                node.right = find(node.right)
                return node
            elif node.val > key:
                node.left = find(node.left)
                return node
            else:
                if not node.left and not node.right:
                    return None
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = successor(node.left)
                temp.right = node.right
                return node.left
            
        return find(root)
        
                