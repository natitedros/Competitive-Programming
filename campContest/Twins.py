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
coins = inlt()
coins.sort()
sm = sum(coins)
half = sm/2
right = n-1
res = 0
count = 0
while right >= 0 and res<=half:
    res += coins[right]
    right -= 1
    count += 1
print(count)