import sys
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
test = inp()
for k in range(test):
    n = inp()
    set1 = set()
    set2 = set()
    possible = True
    for i in range(n):
        a,b = invr()
        if (a == b) or (a in set1 and a in set2) or (b in set1 and b in set2) or (a in set1 and b in set2) or (b in set1 and a in set2):
            possible = False
        if a in set1 or b in set1:
            set2.add(a)
            set2.add(b)
        elif a in set2 or b in set2:
            set1.add(a)
            set1.add(b)
        else:
            if len(set1) > len(set2):
                set2.add(a)
                set2.add(b)
            else:
                set1.add(a)
                set1.add(b)
    if not possible:
        print("NO")
    else:
        print("YES")