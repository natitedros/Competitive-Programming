# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        node = root
        q = deque()
        q.append((node,0,1))
        res = 1
        minNode,maxNode = 1,1
        prevLvl = 0
        while q:
            node,level,num = q.popleft()
            if level != prevLvl:
                prevLvl = level
                res = max(res,maxNode-minNode+1)
                minNode = num
            maxNode = num
            if node.left:
                q.append((node.left,level+1,(2*num)-1))
            if node.right:
                q.append((node.right,level+1,(2*num)))
        return max(res,maxNode-minNode+1)