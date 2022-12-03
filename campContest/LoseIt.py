import sys, threading, heapq, math
from collections import defaultdict
input = sys.stdin.readline


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    vals = set([4,8,15,16,23,42])
    freq = [0 for _ in range(6)]
    res = 0
    for num in nums:
        if num == 4:
            freq[0] += 1
        if num == 8:
            if freq[0] > freq[1]:
                freq[1] += 1
            else:
                res += 1
        elif num == 15:
            if freq[1] > freq[2]:
                freq[2] += 1
            else:
                res += 1
        elif num == 16:
            if freq[2] > freq[3]:
                freq[3] += 1
            else:
                res += 1
        elif num == 23:
            if freq[3] > freq[4]:
                freq[4] += 1
            else:
                res += 1
        elif num == 42:
            if freq[4] > freq[5]:
                freq[5] += 1
            else:
                res += 1
    minFreq = min(freq)
    for f in freq:
        res += f - minFreq
    print(res)
    
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    