import sys
from tkinter.messagebox import YES
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
days, m = invr()
gap = []
for i in range(m):
    gap.append(inlt())
gap.sort()
dicts = {}
