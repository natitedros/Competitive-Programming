class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        def sumFinder(head,targetSum):
            targetSum -= head.val
            if head.left:
                if sumFinder(head.left,targetSum):
                    return True
            if head.right:
                if sumFinder(head.right,targetSum):
                    return True
            if not head.left and not head.right:
                if targetSum == 0:
                    return True
                return False
        return sumFinder(root,targetSum)