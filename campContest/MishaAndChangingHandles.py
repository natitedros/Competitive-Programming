import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(str,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
n = inp()
d = {}
for i in range(n):
    arr = inlt()
    d[arr[0]] = arr[1]
    d[arr[1]] = arr[1]
count = 0
paths = set()
for key in d:
    if key == d[key]:
        count += 1
print(count)
def find(key):
    if d[key] == key:
        return key
    return find(d[key])
for key in d.keys():
    temp = find(key)
    if temp not in paths:
        paths.add(temp)
        print(key +" "+ temp)