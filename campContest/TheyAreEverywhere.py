import sys,heapq
from collections import defaultdict,deque
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input().strip()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

n = inp()
flats = insr()
minFlat = n
total = set(flats)
left = 0
window = set()
freq = defaultdict(int)

for right in range(n):
    window.add(flats[right])
    freq[flats[right]] += 1
    while len(window) == len(total):
        minFlat = min(minFlat,right-left+1)
        freq[flats[left]] -= 1
        if not freq[flats[left]]:
            window.remove(flats[left])
        left += 1
        
print(minFlat)
