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
test = inp()
for k in range(test):
    w = insr()
    p = inp()
    s = sorted(w,reverse=True)
    sm = 0
    for char in w:
        sm += ord(char)-96
    freq = defaultdict(int)
    ptr = 0
    while sm>p:
        sm -= (ord(s[ptr])-96)
        freq[s[ptr]] += 1
        ptr += 1
    res = ""
    for char in w:
        if freq[char] == 0:
            res += char
        else:
            freq[char] -= 1
    print(res)
