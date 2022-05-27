class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        leftPref = []
        for i in range(l):
            if not leftPref:
                leftPref.append(nums[i])
            else:
                leftPref.append(leftPref[-1]+nums[i])
        res = -1
        ptr = 0
        while ptr < l:
            if ptr == 0:
                if leftPref[-1]-leftPref[0] == 0:
                    res = ptr
                    break
            elif ptr == l-1:
                if leftPref[ptr-1] == 0:
                    res = ptr
                    break
            else:
                if leftPref[ptr-1] == leftPref[-1]-leftPref[ptr]:
                    res = ptr
                    break
            ptr += 1
        return res