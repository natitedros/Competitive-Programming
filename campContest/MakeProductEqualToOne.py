import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

n = inp()
nums = inlt()
negs = 0
minPos = 0
maxNeg = 0
for i in range(n):
    if nums[i] < 0:
        negs += 1
        if nums[i] > nums[maxNeg] or nums[maxNeg] > 0:
            maxNeg = i
    else:
        if nums[i] < nums[minPos] or nums[minPos] < 0:
            minPos = i
res = 0
if negs%2 != 0:
    temp = 0
    if nums[minPos] < abs(nums[maxNeg]):
        temp = minPos
    else:
        temp = maxNeg
    for i in range(n):
        if i == temp:
            if nums[temp] >= 0:
                res += abs(nums[i]+1)
            else:
                res += abs(nums[i]-1)
        elif nums[i] < 0:
            res += abs(nums[i]+1)
        else:
            res += abs(nums[i]-1)
else:
    for i in range(n):
        if nums[i] < 0:
            res += abs(nums[i]+1)
        else:
            res += abs(nums[i]-1)
print(res)