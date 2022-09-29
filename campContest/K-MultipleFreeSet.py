import sys
from collections import defaultdict
import math
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
n,k = invr()
nums = inlt()
nums.sort()
numbers = 0
multiples = set()
for i in range(n):
    if nums[i] in multiples:
        continue
    else:
        numbers += 1
        multiples.add(nums[i]*k)
print(numbers)
    
    