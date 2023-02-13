import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        res = []
        heap = []
        for i in range(n):
            if nums[i] > 0:
                heapq.heappush(heap, [-nums[i],i])
        while len(heap) > 1:
            num1, ind1 = heapq.heappop(heap)
            num2, ind2 = heapq.heappop(heap)
            res.append([ind1+1, ind2+1])
            num1 += 1
            num2 += 1
            if num1 < 0:
                heapq.heappush(heap, [num1, ind1])
            if num2 < 0:
                heapq.heappush(heap, [num2, ind2])
        print(len(res))
        for inds in res:
            print(inds[0],inds[1])
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    