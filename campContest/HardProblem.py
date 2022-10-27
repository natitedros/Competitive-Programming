import sys,heapq
from collections import defaultdict,deque
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
def invr():
    return(map(int,input().split()))

def dfs(stringNumber, reverseCost, string, isReversed, index, dp):
    if (isReversed,index) in dp:
        return dp[(isReversed,index)]
    if index == stringNumber-1:
        if isReversed:
            return reverseCost[index]
        return 0
    dp[(isReversed,index)] = math.inf
    current = string[index].copy()
    cost = 0
    if isReversed:
        current.reverse()
        cost = reverseCost[index]
    if current <= string[index+1]:
        temp = dfs(stringNumber, reverseCost, string, False, index+1, dp)
        dp[(isReversed, index)] = min(dp[(isReversed, index)], temp)
    rev = string[index+1].copy()
    rev.reverse()
    if current <= rev:
        temp = dfs(stringNumber, reverseCost, string, True, index+1, dp)
        dp[(isReversed, index)] = min(dp[(isReversed, index)], temp)
    
    dp[(isReversed, index)] += cost
    return dp[(isReversed, index)]


            
def main():
    stringNumber = inp()
    reverseCost = inlt()
    strings = []
    for _ in range(stringNumber):
        strings.append(insr())
    answer = min(reverseCost[0]+dfs(stringNumber, reverseCost, strings, True, 0, {}), dfs(stringNumber, reverseCost, strings, False, 0, {}))
    if answer == math.inf:
        print(-1)
    else:
        print(answer)
            
main()

# def bfs(stringNumber, reverseCost, strings):
#     queue = deque()
#     queue.append((strings[0], 0, 0))
#     queue.append((strings[0][::-1], 0, reverseCost[0]))
#     result = math.inf
#     while queue:
#         length = len(queue)
#         while length:
#             length -= 1
#             word, index, cost = queue.popleft()
#             if index < stringNumber-1:
#                 if word <= strings[index+1]:
#                     queue.append((strings[index+1], index+1, cost))
#                 rev = strings[index+1][::-1]
#                 if word <= rev:
#                     queue.append((rev, index+1, cost+reverseCost[index+1]))
#             else:
#                 result = min(result, cost)
            
#     return result

