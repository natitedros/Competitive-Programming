import sys
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
test = inp()
for k in range(test):
    n = inp()
    nums = inlt()
    left,right = 0, 0
    numbers = set()
    while right < n:
        while nums[right] in numbers:
            numbers.remove(nums[left])
            left += 1
        numbers.add(nums[right])
        right += 1
    print(n-len(numbers))