class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        def depthFinder(root):
            if len(root.children) == 0:
                return 1
            depth = 0
            for child in root.children:
                depth = max(depth, 1+depthFinder(child))
            return depth
        return depthFinder(root)