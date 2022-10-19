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
    return(list(s[:len(s)-1]))
def invr():
    return(map(int,input().split()))

def main():
    N, k = invr()
    nums = inlt()
    nums.sort()
    maxFreqVal = 0
    maxFreq = 0
    
    left = 0
    moves = 0
    previous = 0
    
    for right in range(N):
        
        moves += (nums[right]-previous)*(right-left)
        
        while moves > k:
            moves -= nums[right]-nums[left]
            left += 1
            
        previous = nums[right]
        
        if right-left+1 > maxFreq:
            maxFreq = right-left+1
            maxFreqVal = nums[right]
            
    print(maxFreq, maxFreqVal)
    
            
main()

