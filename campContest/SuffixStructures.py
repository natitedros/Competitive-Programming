import sys, threading, heapq, math
from collections import defaultdict, Counter
input = sys.stdin.readline


def main():
    s = input().strip()
    t = input().strip()
    needTree = False
    setS = set()
    setT = set()
    for char in s:
        setS.add(char)
    for char in t:
        setT.add(char)
        if char not in setS:
            needTree = True
            break
    if needTree:
        print("need tree")
    else:
        Sptr, Tptr = 0, 0
        automation = False
        while Sptr < len(s) and Tptr < len(t):
            while Sptr < len(s) and s[Sptr] != t[Tptr]:
                Sptr += 1
            if Sptr < len(s) and Tptr == len(t)-1:
                automation = True
            Tptr += 1
            Sptr += 1
        if automation:
            print("automaton")
        elif setS == setT and len(s) == len(t):
            print("array")
        elif len(s) > len(t):
            print("both")
        else:
            print("need tree")
                
main()
       
# threading.stack_size(1 << 27)
# sys.setrecursionlimit(1 << 30)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
    