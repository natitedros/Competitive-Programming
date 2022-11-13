import sys, threading
from collections import defaultdict
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
    
def sortCost(l, r, nums):
    if r-l == 1:
        if nums[l] + 1 == nums[r]:
            return [nums[l], nums[r], 0]
        elif nums[r]+1 == nums[l]:
            return [nums[r], nums[l], 1]
        else:
            return [-1, -1, -1]
    mid = l + (r-l)//2
    left = sortCost(l, mid, nums)
    right = sortCost(mid + 1, r, nums)
    
    if left == [-1, -1, -1] or right == [-1, -1, -1]:
        return [-1, -1, -1]
    cost = left[2] + right[2]
    if left[1] + 1 == right[0]:
        return [left[0], right[1], cost]
    elif right[1] + 1 == left[0]:
        return [right[0], left[1], cost+1]
    else:
        return [-1, -1, -1]

def main():
    for _ in range(inp()):
        n = inp()
        nums = inlt()
        if n == 1:
            print(0)
        else:
            answer = sortCost(0, n-1, nums)
            print(answer[2])
        
threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
    