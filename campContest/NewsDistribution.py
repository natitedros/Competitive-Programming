import sys, threading, heapq, math
from collections import defaultdict
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    parent = [0]*(n+1)
    rank = [1]*(n+1)
    for i in range(1, n+1):
        parent[i] = i
        
    def find(person):
        if person == parent[person]:
            return person
        parent[person] = find(parent[person])
        return parent[person]
    
    def union(p1, p2):
        parent1 = find(p1)
        parent2 = find(p2)
        if parent1 == parent2:
            return
        if rank[parent1] < rank[parent2]:
            parent[parent1] = parent2
            rank[parent2] += rank[parent1]
        else:
            parent[parent2] = parent1
            rank[parent1] += rank[parent2]

    for _ in range(m):
        group = list(map(int, input().split()))
        if group[0] > 1:
            for i in range(2, group[0]+1):
                union(group[1], group[i])
    
    result = []
    for i in range(1, n+1):
        result.append(rank[find(i)])
    print(*result)
    
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    