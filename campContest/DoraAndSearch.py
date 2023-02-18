import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        left, right = 0, n-1
        found = False
        minVal, maxVal = 1, n
        while left < right:
            leftValid = minVal < nums[left] < maxVal
            rightValid = minVal < nums[right] < maxVal
            if leftValid and rightValid:
                print(left+1, right+1)
                found = True
                break
            if not leftValid:
                if nums[left] == minVal:
                    minVal += 1
                else:
                    maxVal -= 1
                left += 1
            if not rightValid:
                if nums[right] == minVal:
                    minVal += 1
                else:
                    maxVal -= 1
                right -= 1
        if not found:
            print(-1)
    
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    