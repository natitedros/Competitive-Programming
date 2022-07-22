class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxQ = deque()
        left,right = 0,0
        res = []
        while right < k:
            while maxQ and nums[maxQ[-1]] < nums[right]:
                maxQ.pop()
            maxQ.append(right)
            right += 1
        res.append(nums[maxQ[0]])
        if left == maxQ[0]:
            maxQ.popleft()
        left += 1
        while right < len(nums):
            while maxQ and nums[maxQ[-1]] < nums[right]:
                maxQ.pop()
            maxQ.append(right)
            res.append(nums[maxQ[0]])
            if left == maxQ[0]:
                maxQ.popleft()
            left += 1
            right += 1
        return res