# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append((root,0))
        n = 0
        res = []
        currentLvl = 0
        maxVal = -(2**31)
        while q:
            node, lvl = q.popleft()
            if currentLvl == lvl:
                if node.val > maxVal:
                    maxVal = node.val
            else:
                currentLvl = lvl
                res.append(maxVal)
                maxVal = node.val
            if node.left:
                q.append((node.left,lvl+1))
            if node.right:
                q.append((node.right,lvl+1))
        res.append(maxVal)
        return res