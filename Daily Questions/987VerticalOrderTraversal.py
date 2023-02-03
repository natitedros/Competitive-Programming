# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        minCol,maxCol = inf,-inf
        def dfs(node,row,col):
            nonlocal minCol,maxCol
            if not node:
                return
            res[col].append((row,node.val))
            minCol = min(col,minCol)
            maxCol = max(col,maxCol)
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        dfs(root,0,0)
        ans = []
        for i in range(minCol,maxCol+1):
            res[i].sort()
            temp = []
            for row,val in res[i]:
                temp.append(val)
            ans.append(temp)
        return ans