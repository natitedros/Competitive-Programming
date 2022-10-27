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
     
def LPS(string):
    prefix = [0]*len(string)
    left = 0
    for right in range(1,len(string)):
        while left > 0 and string[left] != string[right]:
            left = prefix[left-1]
        if string[left] == string[right]:
            prefix[right] += left+1
            left += 1
        else:
            prefix[right] = 0
            
    return prefix
       
def main():
    string = insr()
    prefSuf = LPS(string)
    print(prefSuf)
            
main()

