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
test = inp()
for k in range(test):
    n = inp()
    nums = inlt()
    res = 0
    numFound = False
    for i in range(n-1):
        if numFound and nums[i] == 0:
            res += 1
        elif nums[i] != 0:
            numFound = True
            res += nums[i]
    print(res)