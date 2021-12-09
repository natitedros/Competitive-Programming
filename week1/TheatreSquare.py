import math
inp = input().rstrip().split(' ')
def noOfSquares(n ,m ,a):
    al = 0
    aw = 0
    if n/a > n//a:
        al = math.ceil(n/a)
    else:
        al = math.floor(n/a)
    if m/a > m//a:
        aw = math.ceil(m/a)
    else:
        aw = math.floor(m/a)
    return al*aw
print(noOfSquares(int(inp[0]), int(inp[1]), int(inp[2])))
