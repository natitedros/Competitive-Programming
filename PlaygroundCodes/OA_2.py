import math
from collections import defaultdict
def solve(nums):
    freq = defaultdict(int)
    sides = []
    for num in nums:
        freq[num] += 1
        if freq[num] == 4:
            return 0
        if freq[num] == 2:
            sides.append(num)
    minDistance = math.inf
    sides.sort()
    for i in range(1, len(sides)):
        minDistance = min(minDistance, sides[i]-sides[i-1])
    return minDistance if minDistance != math.inf else -1
print(solve([4,1,1,1]))
