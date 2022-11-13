import sys
import threading
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
    for _ in range(inp()):
        nk = input().split()
        n = int(nk[0])
        k = nk[1]
        s = insr()
        if k == "g":
            print(0)
        else:
            start = -1
            found = True
            maxTime = 0
            for i in range(n):
                if found and s[i] == k:
                    found = False
                    start = i
                elif not found and s[i] == "g":
                    found = True
                    maxTime = max(maxTime, i-start)
                    start = -1
            if not found:
                for i in range(n):
                    if s[i] == "g":
                        found = True
                        maxTime = max(maxTime, n+i-start)
                        break
            
            print(maxTime)
                
threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
    