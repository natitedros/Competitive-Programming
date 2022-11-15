import math
from collections import defaultdict
def solve(nums):
    freq = defaultdict(int)
    lengths = []
    for num in nums:
        freq[num] += 1
        if freq[num]%2 == 0:
            lengths.append(num)
    if len(lengths) < 2:
        return -1
    lengths.sort()
    minDistance = math.inf
    for i in range(1, len(lengths)):
        minDistance = min(minDistance, lengths[i]-lengths[i-1])
    return minDistance
