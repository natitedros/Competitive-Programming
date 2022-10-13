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
    n,e = invr()
    neigh = defaultdict(list)
    sets = defaultdict(set)
    for i in range(e):
        u,v = invr()
        neigh[u].append(v)
        neigh[v].append(u)
    sign = [None]*(n+1)
    visited = set()
    possible = True
    def bfs(node):
        nonlocal possible,visited,sign
        q = deque()
        q.append(node)
        visited.add(node)
        sign[node] = True
        sets[True].add(node)
        while q:
            node = q.popleft()
            for neighbor in neigh[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    sign[neighbor] = not sign[node]
                    sets[sign[neighbor]].add(neighbor)
                    q.append(neighbor)
                elif neighbor in visited and sign[neighbor] == sign[node]:
                    possible = False
                    break
    for i in range(1,n+1):
        if i not in visited and neigh[i]:
            bfs(i)
    if not possible:
        print(-1)
    else:
        print(len(sets[True]))
        print(*sets[True])
        print(len(sets[False]))
        print(*sets[False])
main()
    

