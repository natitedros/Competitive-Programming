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

n, k = invr()
sum = k
i = 0
while sum<240 and i <= n:
    i+=1
    sum += 5*i
if sum<=240 and i <= n:
    print(i)
else:
    print(i-1)
