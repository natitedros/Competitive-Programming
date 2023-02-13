import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        look = input().strip()
        sums = []
        for i in range(n):
            if look[i] == "L":
                sums.append(i)
            else:
                sums.append(n-i-1)
        final = []
        for i in range(n):
            final.append(max(i,n-i-1))
        res = []
        left, right = 0, n-1
        total = sum(sums)
        for i in range(n//2):
            if final[i] != sums[i]:
                total += final[i] - sums[i]
                res.append(total)
            if final[n-i-1] != sums[n-i-1]:
                total += final[n-i-1] - sums[n-i-1]
                res.append(total)
        while len(res) < n:
            res.append(total)
        print(*res)
        
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    