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
    ticket = insr()
    s1 = int(ticket[0])+int(ticket[1])+int(ticket[2])
    s2 = int(ticket[3])+int(ticket[4])+int(ticket[5])
    if s1 == s2:
        print("YES")
    else:
        print("NO")