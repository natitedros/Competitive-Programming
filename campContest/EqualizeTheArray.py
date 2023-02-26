import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            
        freqGroup = defaultdict(int)
        for key in freq.keys():
            freqGroup[freq[key]] += 1
            
        freqKeys = sorted(key for key in freqGroup)
        
        cost1 = [0] * len(freqKeys)
        prev = freqKeys[0] * freqGroup[freqKeys[0]]
        for i in range(1, len(freqKeys)):
            cost1[i] = cost1[i-1] + prev
            prev = freqKeys[i] * freqGroup[freqKeys[i]]
        cost2 = [0] * len(freqKeys)
        prev = freqGroup[freqKeys[-1]]
        for i in range(len(freqKeys)-2, -1, -1):
            cost2[i] += ((freqKeys[i+1] - freqKeys[i]) * prev) + cost2[i+1]
            prev += freqGroup[freqKeys[i]]
        ans = math.inf
        for i in range(len(freqKeys)):
            ans = min(ans, cost1[i] + cost2[i])
        print(ans)
        
    
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    