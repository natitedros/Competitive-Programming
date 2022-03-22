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

n = inp()
arr = inlt()

maxSushi = 0
oneCount = 0
twoCount = 0
i = 0
while i < n:
    if arr[i] == 1:
        oneCount+=1
    elif arr[i] == 2:
        twoCount+=1
    if i == n-1 or arr[i] != arr[i+1]:
        if 2*min(oneCount,twoCount) > maxSushi:
            maxSushi = 2*min(oneCount,twoCount)
        if arr[i] == 1:
            twoCount = 0
        else:
            oneCount = 0
    i += 1
print(maxSushi)

