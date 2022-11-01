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
    
    
def main():
    n, m, k = inlt()
    result = 0
    graph = defaultdict(list)
    for _ in range(m):
        u, v, cost = inlt()
        graph[u].append((v, cost))
    trainPath = [-1]*(n+1)
    for _ in range(k):
        city, train = invr()
        if trainPath[city] != -1:
            result += 1
            trainPath[city] = min(train, trainPath[city])
        else:
            trainPath[city] = train
        
    shortestPath = [math.inf]*(n+1)
    shortestPath[1] = 0
    queue = []
    visited = set()
    queue.append((0, 1))
    while queue:
        path, city = heapq.heappop(queue)
        shortestPath[city] = path
        visited.add(city)
        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                if cost+path < shortestPath[neighbor]:
                    shortestPath[neighbor] = cost+path
                    heapq.heappush(queue, (cost+path, neighbor))
    
    for i in range(1,n+1):
        
        if trainPath[i] > 0 and shortestPath[i] <= trainPath[i]:
            result += 1
    print(result)
    
main()