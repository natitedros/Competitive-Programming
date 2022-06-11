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
rounds = inp()
d = {}
winner = ""
for i in range(rounds):
    temp = input().strip().split()
    if temp[0] not in d:
        d[temp[0]] = 0
    d[temp[0]] += int(temp[1])
    if winner == "" or d[winner] < d[temp[0]]:
        winner = temp[0]
print(winner)