import sys
from tkinter.messagebox import YES
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

n, m = invr()
diff = inlt()
minDiff = min(diff)
diff.sort()
midVal = m//2
q = []
for i in range(n):
    q.append(inp())
i = 0
for i in range(len(q)):
    if q[i]<=minDiff:
        print("NO")
    else:
        if q[i] > diff[midVal]:
            print("NO")
        else:
            print("YES")
        # left = 0
        # right = m-1
        # mid = 0
        # while left<=right:
        #     mid = left+(right-left)//2
        #     if diff[mid] < q[i]:
        #         left = mid+1
        #     elif diff[mid] > q[i]:
        #         right = mid-1
        #     else:
        #         break
        #     if diff[mid] < q[i]:
        #         mid+=1
        #     if n-(mid)>n/2:
        #         print("YES")
        #     else:
        #         print("NO")
    

