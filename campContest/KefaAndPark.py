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
    return(list(s[:len(s)-1]))
def invr():
    return(map(int,input().split()))
def numberOfPaths(neighbor, hasCats, v, maxStreak):
    queue = deque()
    visited = set()
    queue.append((v,0))
    pathCount = 0
    while queue:
        vertex, streak = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            if hasCats[vertex]:
                streak += 1
            else:
                streak = 0
            if streak <= maxStreak:
                if len(neighbor[vertex]) == 1 and vertex != 1:
                    pathCount += 1
                else:
                    for child in neighbor[vertex]:
                        queue.append((child,streak))
    return pathCount

def main():
    vertices, catLimit = invr()
    hasCats = [0]+inlt()
    neighbor = defaultdict(list)
    for _ in range(vertices-1):
        vertex1, vertex2 = invr()
        neighbor[vertex1].append(vertex2)
        neighbor[vertex2].append(vertex1)
    answer = numberOfPaths(neighbor, hasCats, 1, catLimit)
    print(answer)
    
main()

