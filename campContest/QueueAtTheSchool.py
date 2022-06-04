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

n, t = invr()
queue = insr()
d = set()
for i in range(n):
    if queue[i] == "B":
        d.add(i)
while t > 0:
    val = 0
    while val < n:
        if val+1 < n and queue[val+1] == "G":
            queue[val], queue[val+1] = queue[val+1], queue[val]
            val += 1
        val += 1
    t -= 1
print(''.join(queue))