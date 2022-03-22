class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        res = True
        q.append([root.left,root.right])
        while q:
            l,r = q.popleft()
            if not l and not r:
                continue
            if not l or not r:
                res = False
                break
            if l.val == r.val:
                q.append([l.left,r.right])
                q.append([l.right,r.left])
            else:
                res = False
                break
        return res