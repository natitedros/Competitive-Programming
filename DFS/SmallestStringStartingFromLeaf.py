# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = [26]
        def dfs(node,path):
            nonlocal res
            if not node.left and not node.right:
                res = min(res,(path+[node.val])[::-1])
                return
            if node.left:
                dfs(node.left,path+[node.val])
            if node.right:
                dfs(node.right,path+[node.val])
        
        dfs(root,[])
        ans = [] 
        for char in res:
            ans.append(chr(char+97))
        return ''.join(ans)
