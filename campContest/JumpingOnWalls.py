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
n, k = invr()
left = insr()
right = insr()
d = {}
def dfs(lt,ind,water):
    if(lt,ind,water) in d:
        return d[(lt,ind,water)]
    if ind >= n:
        return True
    wall = []
    if lt:
        wall = left
    else:
        wall = right
    if  wall[ind] == "X" or ind <= water:
        return False
    temp = False
    temp |= dfs(lt,ind+1,water+1)
    temp |= dfs(lt,ind-1,water+1)
    temp |= dfs(not lt,ind+k,water+1)
    d[(lt,ind,water)] = temp
    return temp
if dfs(True,0,-1):
    print("YES") 
else:
    print("NO")