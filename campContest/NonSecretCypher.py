import sys,heapq
from collections import defaultdict,deque
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
def main():
    n,k = invr()
    nums = inlt()
    freq = defaultdict(int)
    left = 0
    res = 0
    for right in range(n):
        freq[nums[right]] += 1
        while freq[nums[right]] == k:
            res += n-right
            freq[nums[left]] -= 1
            left += 1
    print(res)
main()
