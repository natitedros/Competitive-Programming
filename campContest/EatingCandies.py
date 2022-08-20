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
    arr = inlt()
    left, right = 0, n-1
    alice = arr[left]
    bob = arr[right]
    count = 2
    res = 0
    while left < right:
        if alice > bob:
            right -= 1
            bob += arr[right]
            count += 1
        elif bob > alice:
            left += 1
            alice += arr[left]
            count += 1
        else:
            res = count
            left += 1
            alice+=arr[left]
            right -= 1
            bob += arr[right]
            count += 2
    print(res)