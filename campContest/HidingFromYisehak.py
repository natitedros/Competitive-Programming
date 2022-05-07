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
for i in range(test):
    n = inp()
    height = inlt()
    j = n-1
    maxHeight = height[-1]
    counter = 0
    while j >= 0:
        if height[j] < maxHeight:
            counter += 1
        else:
            maxHeight = height[j]
        j -= 1
    print(counter)