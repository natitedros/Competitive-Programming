from collections import Counter
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
    n = inp()
    nums = inlt()
    k = (sum(nums)/n)*2
    freq = Counter(nums)
    res = 0
    for num in nums:
        freq[num]-=1
        if k-num in freq and freq[k-num] > 0:
            res += freq[k-num]
    print(res)