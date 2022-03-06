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
days, m = invr()
gap = []
for i in range(m):
    gap.append(inlt())
gap.sort()
i=0
j=0
while (i< len(gap)-1) :
    if(gap[i][0]==gap[i+1][0]):
        gap.pop(i)
        i=i-1
    i=i+1
while j<len(gap)-1:
    if gap[j][1]>=gap[j+1][1]:
        gap.pop(j+1)
        continue
    if gap[j][1]>=gap[j+1][0]:
        gap[j][1]=gap[j+1][1]
        gap.pop(j+1)
        j=j-1
    j=j+1
count = 0
for i in range(len(gap)):
    for j in range(gap[i][0],gap[i][1]+1):
        count += 1
if count < days:
    print("YES")
else:
    print("NO")