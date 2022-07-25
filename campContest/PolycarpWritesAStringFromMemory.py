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
    day = set()
    res = 0
    for char in s:
        day.add(char)
        if len(day) == 4:
            day = set()
            day.add(char)
            res += 1
    if len(day):
        res += 1
    print(res)