import sys
input = sys.stdin.readline
from collections import defaultdict

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
length = defaultdict(int)
index = {}
for i in range(n):
    length[nums[i]] = 1+length[nums[i]-1]
    if nums[i]-1 in index:
        index[nums[i]] = index[nums[i]-1]
        index[nums[i]].append(i)
    else:
        index[nums[i]] = [i]
maxLen = 0
maxIndex = []
for i in range(n):
    if length[nums[i]] > maxLen:
        maxLen = length[nums[i]]
        maxIndex = index[nums[i]]
print(maxLen)
for i in range(maxLen):
    print(maxIndex[i]+1, end=" ")