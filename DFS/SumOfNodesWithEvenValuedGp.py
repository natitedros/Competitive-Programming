class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        node = root
        p = None
        gp = None
        sm = 0
        def calculateSum(node,p,gp):
            nonlocal sm
            if gp != None and gp%2 == 0:
                sm += node.val
            if node.left:
                calculateSum(node.left,node.val,p)
            if node.right:
                calculateSum(node.right,node.val,p)
        calculateSum(node,p,gp)
        return sm