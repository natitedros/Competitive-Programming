import sys
from collections import defaultdict
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
n,m = invr()
d = defaultdict(set)
for i in range(1,n+1):
    d[i+1] = set(inlt()[1:])
parent = [0]*n
rank = [1]*n
joined = set()
for i in range(n):
    parent[i] = i
def find(city):
    if city == parent[city]:
        return city
    return find(parent[city])
def union(one, two):
    parentOne = find(one)
    parentTwo = find(two)
    if parentOne == parentTwo:
        return 0
    if rank[parentOne] > rank[parentTwo]:
        parent[parentTwo] = parentOne
    elif rank[parentTwo] > rank[parentOne]:
        parent[parentOne] = parentTwo
    else:
        parent[parentTwo] = parentOne
        rank[parentOne] += 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j and (i,j) not in joined:
            for lang in d[j]:
                if lang in d[i]:
                    joined.add((j,i))
                    union(i, j)
count = 0
for i in range(n):
    if parent[i] == i:
        count += 1
print(count-1)
