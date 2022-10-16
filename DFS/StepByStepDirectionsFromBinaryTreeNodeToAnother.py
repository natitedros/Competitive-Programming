# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        found = False
        commonAns = TreeNode(-1)
        def LCA(node):
            nonlocal found,commonAns
            if found:
                return
            if not node:
                return False
            isNode = False
            if node.val == startValue or node.val == destValue:
                isNode = True
            left = LCA(node.left)
            right = LCA(node.right)
            if (isNode and left) or (isNode and right) or (left and right):
                commonAns = node
                found = True
            return isNode or left or right
        LCA(root)
        def findStart(node):
            if not node:
                return inf
            if node.val == startValue:
                return 0
            return 1+min(findStart(node.left),findStart(node.right))
        height = findStart(commonAns)
        res = ["U"]*height
        def findDest(node,path):
            nonlocal res
            if not node:
                return
            if node.val == destValue:
                res += path
                return
            path.append("L")
            findDest(node.left,path)
            path.pop()
            path.append("R")
            findDest(node.right,path)
            path.pop()
        findDest(commonAns,[])
        return ''.join(res)

# Edited
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        targetPaths = []
        def pathBuild(target,node,path):
            if not node:
                return
            if node.val == target:
                targetPaths.append(path.copy())
                return
            path.append("L")
            pathBuild(target,node.left,path)
            path.pop()
            path.append("R")
            pathBuild(target,node.right,path)
            path.pop()
        pathBuild(startValue,root,[])
        pathBuild(destValue,root,[])
        lens = len(targetPaths[0])
        lend = len(targetPaths[1])
        ptr = 0
        while ptr < lens and ptr < lend and targetPaths[0][ptr] == targetPaths[1][ptr]:
            ptr += 1
        start = ["U"]*(lens-ptr)
        dest = targetPaths[1][ptr:]
        return ''.join(start+dest)