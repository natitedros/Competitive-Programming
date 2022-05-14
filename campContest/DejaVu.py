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
    s = input()
    lens = len(s)
    if s == "a"*lens:
        print("NO")
    elif lens%2==0:
        print("YES")
        print("a"+s)
    else:
        left = 0
        right = lens-1
        while s[left] == 'a':
            left += 1
        
    