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
    for _ in range(inp()):
        nr = inp()
        red = inlt()
        nb = inp()
        blue = inlt()
        maxSubA = 0
        prev = 0
        for num in red:
            prev += num
            maxSubA = max(maxSubA, prev)
        prev = 0
        maxSubB = 0
        for num in blue:
            prev += num
            maxSubB = max(maxSubB, prev)
        print(maxSubA+maxSubB)
            
main()        
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    