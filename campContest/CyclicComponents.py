import sys, threading, heapq
from collections import defaultdict
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
def main():
    
    v, e = map(int,input().split())
    graph = defaultdict(list)
    for k in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    possible = []
    for key in graph.keys():
        if len(graph[key]) == 2:
            possible.append(key)
    visited = set()
    def rec(node, parent):
        if len(graph[node]) != 2:
            return 0
        if node in visited:
            return 1
        visited.add(node)
        for key in graph[node]:
            if key != parent:
                return rec(key, node)
    result = 0 
    for p in possible:
        if p not in visited:
            result += rec(p, graph[p][0])
    print(result)

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
    