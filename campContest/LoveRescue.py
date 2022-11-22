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
    n = inp()
    a = insr()
    b = insr()
    path = defaultdict(list)
    result = []
    
    def isFound(current, target):
        if current == target:
            return True
        for neigh in path[current]:
            if neigh not in visited:
                visited.add(neigh)
                if isFound(neigh, target):
                    return True
        return False
        
    for i in range(n):
        visited = set()
        if not isFound(a[i], b[i]):
            path[a[i]].append(b[i])
            path[b[i]].append(a[i])
            result.append([a[i], b[i]])
    print(len(result))
    for char1, char2 in result:
        print(char1, char2)
        
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    