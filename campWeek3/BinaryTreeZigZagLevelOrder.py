class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        distance = 0
        q.append((root,distance))
        stk = []
        res = []
        while q:
            (node,dist) = q.popleft()
            if dist != distance:
                if distance%2==0:
                    res.append(stk)
                else:
                    stk.reverse()
                    res.append(stk)
                stk = []
                distance = dist
            stk.append(node.val)
            if node.left:
                q.append((node.left, dist+1))
            if node.right:
                q.append((node.right, dist+1))
        if distance%2==0:
            res.append(stk)
        else:
            stk.reverse()
            res.append(stk)
        return res