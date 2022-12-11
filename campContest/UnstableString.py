import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        bits = input().strip()
        dp = [[0 for _ in range(2)] for _ in range(len(bits))]
        if bits[0] != "0":
            dp[0][1] = 1
        if bits[0] != "1":
            dp[0][0] = 1
        for i in range(1, len(bits)):
            if bits[i] != "0":
                dp[i][1] = 1 + dp[i-1][0]
            if bits[i] != "1":
                dp[i][0] = 1 + dp[i-1][1]
        count = 0
        for row in dp:
            count += max(row)
        print(count)
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    