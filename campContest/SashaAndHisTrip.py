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

cities, tank = invr()
liters = 0
cost = 0
for i in range(1, cities):
    while liters+1 <= min(tank,cities-i):
        liters += 1
        cost += i
    liters -= 1
print(cost)  