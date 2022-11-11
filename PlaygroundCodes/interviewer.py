def solve():
    left = 0
    cost = 0
    minCost = inf
    for right in range(len(nums)):
        if nums[right] == "E":
            cost += 1
        if right-left+1 == k:
            minCost = min(minCost, cost)
            if nums[left] == "E":
                cost -= 1
            left += 1
    return minCost
