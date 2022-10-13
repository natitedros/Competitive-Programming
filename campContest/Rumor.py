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
    
def main():
    n,m = invr()
    heap = []
    cost = [0]+inlt()
        
    friend = defaultdict(list)
    for i in range(m):
        u,v = invr()
        friend[u].append(v)
        friend[v].append(u)
    visited = set()
    ans = 0
    def bfs(person):
        nonlocal ans,visited
        minVal = cost[person]
        q = deque()
        q.append(person)
        while q:
            p = q.popleft()
            minVal = min(minVal,cost[p])
            for f in friend[p]:
                if f not in visited:
                    q.append(f)
                    visited.add(f)
        ans += minVal
            
    for i in range(1,n+1):
        if i not in visited:
            bfs(i)
            visited.add(i)
    print(ans)
main()
    