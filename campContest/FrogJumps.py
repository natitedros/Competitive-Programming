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
    s = insr()
    n = len(s)
    left,right= 0,0
    maxL=0
    temp = 0
    while right < n:
        if s[right] == "R":
            maxL = max(maxL,temp)
            left = right+1
            temp = 0
        else:
            temp += 1
        right += 1
    maxL = max(maxL,temp)
    print(maxL+1)

# Improved

test_cases = int(input())
for i in range (test_cases):
    board = list(map(len, input().split('R')))
    print(max(board) + 1)
    print(board)