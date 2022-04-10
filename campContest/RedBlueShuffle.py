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

numOfPlay = inp()
res = []
for i in range(numOfPlay):
    cardNo = inp()
    red = input()
    blue = input()
    score = 0
    for j in range(cardNo):
        if red[j] > blue[j]: 
            score -= 1
        elif blue[j] > red[j]:
            score += 1
    if score < 0:
        res.append("RED")
    elif score > 0:
        res.append("BLUE")
    else:
        res.append("EQUAL")
for i in range(len(res)):
    print(res[i])