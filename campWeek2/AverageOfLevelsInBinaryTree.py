class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        res = []
        q.append([root,0])
        sm = 0
        count = 0
        height = 0
        while q:
            node,h = q.popleft()
            if not h == height:
                temp = sm/count
                res.append(float('%.5f'%temp))
                count=0
                sm=0
                height = h
            count += 1
            sm += node.val
            if node.left:
                q.append([node.left,h+1])
            if node.right:
                q.append([node.right,h+1])
        temp = sm/count
        res.append(float('%.5f'%temp))
        return res