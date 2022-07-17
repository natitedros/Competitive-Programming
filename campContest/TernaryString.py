from cmath import inf
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
    d = {'1':0,'2':0,'3':0}
    left = 0
    right = 0
    minLen = inf
    while right < len(s):
        d[s[right]] += 1
        while d['1'] > 0 and d['2'] > 0 and d['3'] > 0:
            minLen = min(minLen,right-left+1)
            d[s[left]] -= 1
            left += 1
        right += 1
    if minLen == inf:
        minLen = 0
    print(minLen)