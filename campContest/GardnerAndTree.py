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
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

test = inp()
for k in range(test):
    input()
    n,k = invr()
    edges = defaultdict(list)
    indegree = [0]*(n+1)
    for e in range(n-1):
        u,v = invr()
        edges[u].append(v)
        indegree[u] += 1
        edges[v].append(u)
        indegree[v] += 1
    q = deque()
    for i in range(1,n+1):
        if indegree[i] <= 1:
            q.append(i)
    count = 0
    removed = set()
    while q:
        if k:
            length = len(q)
            while length:
                node = q.popleft()
                if node not in removed:
                    count += 1
                    removed.add(node)
                    for neigh in edges[node]:
                        indegree[neigh] -= 1
                        if indegree[neigh] <= 1:
                            q.append(neigh)
                length -= 1
            k -= 1
        else:
            q = None
    print(n-count)
        
        
    
    
    

