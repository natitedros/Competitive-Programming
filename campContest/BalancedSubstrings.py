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
        n = inp()
        s = insr()
        found = False
        for l in range(n):
            a = 0
            b = 0
            for r in range(l, n):
                if s[r] == "a":
                    a += 1
                else:
                    b += 1
                if a == b:
                    found = True
                    print(l+1, r+1)
                    break
            if found:
                break
        if not found:
            print(-1, -1)
                
threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
    