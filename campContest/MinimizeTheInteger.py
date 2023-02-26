import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        num = input().strip()
        even, odd = [], []
        for char in num:
            temp = int(char)
            if temp%2:
                odd.append(temp)
            else:
                even.append(temp)
        res = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(even) and ptr2 < len(odd):
            if even[ptr1] < odd[ptr2]:
                res.append(str(even[ptr1]))
                ptr1 += 1
            else:
                res.append(str(odd[ptr2]))
                ptr2 += 1
        while ptr1 < len(even):
            res.append(str(even[ptr1]))
            ptr1 += 1
        while ptr2 < len(odd):
            res.append(str(odd[ptr2]))
            ptr2 += 1
        
        print(''.join(res))
    
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    