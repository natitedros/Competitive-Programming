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
nums = inlt()
pos = sum(nums)//3
print(abs(nums[0]-pos) + abs(nums[1]-pos) + abs(nums[2]-pos))