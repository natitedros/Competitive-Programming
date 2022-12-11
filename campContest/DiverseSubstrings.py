import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        num = input().strip()
        count = defaultdict(int)
        result = 0
        for i in range(n):
            maxFreq = 0
            for j in range(i, min(n, i+100)):
                count[num[j]] += 1
                maxFreq = max(maxFreq, count[num[j]])
                if len(count) >= maxFreq:
                    result += 1
            count.clear()
        print(result)
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    