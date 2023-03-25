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
arr= []
for i in range(n):
    arr.append(inp())
for i in range(len(arr)):
    first = 0
    temp = arr[i]
    curr = 31
    curr2 = 32
    if temp == curr:
        print(31)
    elif temp == curr2:
        print(curr2)
    else:
        while temp > curr:
            curr+=4
            first +=1
        while temp != curr:
            curr-=1
            first += 1
        second = 0
        
        
        while temp>curr2:
            curr2+=4
            second+=1
        while temp!=curr2:
            curr2-=1
            second+=1
        if first<second:
            print(31)
        else:
            print(32) 
