import sys
input = sys.stdin.readline
from collections import defaultdict

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
nums = inlt()
freq = defaultdict(int)
sm = 0
for num in nums:
    sm += num
    freq[num] += 1
visited = set()

for num in nums:
    if num not in visited:
        visited.add(num)
