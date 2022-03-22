class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boat = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
                boat += 1
            else:
                right -= 1
                boat += 1
        return boat