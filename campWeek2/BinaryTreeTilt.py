def sumTilt(sm,head):
    if not head.left and not head.right:
        return [0,head.val]
    elif not head.left:
        right = sumTilt(sm,head.right)
        sm = right[0] + abs(right[1])
        return [sm,head.val+right[1]]
    elif not head.right:
        left = sumTilt(sm,head.left)
        sm = left[0] + abs(left[1])
        return [sm,head.val+left[1]]
    else:
        left = sumTilt(sm,head.left)
        right = sumTilt(sm,head.right)
        sm =  left[0] + right[0] + abs(left[1]-right[1])
        return [sm,head.val+left[1]+right[1]]
    
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sm = 0
        return sumTilt(sm,root)[0]