class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # construct array with values (growthT, plantT)
        # sort in reverse
        # keep track of the current time and blossom time
        arr = []
        for i in range(len(plantTime)):
            arr.append([growTime[i], plantTime[i]])
        arr.sort(reverse=True)
        time = 0
        blossom = 0
        for grow, plant in arr:
            time += plant
            blossom = max(blossom, time+grow)
        return blossom