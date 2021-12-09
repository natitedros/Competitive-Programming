inp = input().rstrip().split(' ')

def dominoNum( m,  n):
    dom = (m*n)//2
    return dom

print(dominoNum(int(inp[0]), int(inp[1])))
