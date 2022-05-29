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
    num = inp()
    res = 0
    for j in range(num.bit_length()-1):
        res <<= 1
        res |= 1
    print(res)