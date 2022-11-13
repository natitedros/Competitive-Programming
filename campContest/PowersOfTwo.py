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
    n, k = map(int,input().split())
    length = n.bit_length()
    ones = bin(n).count("1")
    if ones <= k <= n:
        queue = []
        for i in range(length):
            if n & 1<<i:
                heapq.heappush(queue, -(n & 1<<i))
        while len(queue) < k:
            num = heapq.heappop(queue)
            heapq.heappush(queue, num//2)
            heapq.heappush(queue, num//2)
        for i in range(k):
            queue[i] *= -1
            
        print("YES")
        print(*queue)
        
    else:
        print("NO")
    
      
main()      
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    