from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        for i, num in enumerate(nums):
            if i > indexDiff:
                window.remove(nums[i-indexDiff-1])
            position = bisect_left(window, num)
            if position > 0 and num - window[position-1] <= valueDiff:
                return True
            if position < len(window) and window[position] - num <= valueDiff:
                return True
            window.add(num)
        return False