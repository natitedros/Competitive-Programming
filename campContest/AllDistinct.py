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
        nums = inlt()
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        minus = 0
        unique = 0
        for val in freq.values():
            unique += 1
            if val%2 == 0:
                minus += 1
        print(unique - (minus%2))
            
                
threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
    