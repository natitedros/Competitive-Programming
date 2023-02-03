class Solution:

    def __init__(self, w: List[int]):
        self.weight = [w[0]]
        for i in range(1,len(w)):
            self.weight.append(self.weight[-1]+w[i])
        
    def pickIndex(self) -> int:
        rand = random.randint(1, self.weight[-1])
        left, right = 0, len(self.weight)-1
        while left <= right:
            mid = (left+right)//2
            if self.weight[mid] == rand:
                return mid
            elif self.weight[mid] > rand:
                right = mid - 1
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()