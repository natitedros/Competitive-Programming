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
n, q = invr()
root = [-1]*(n+1)
rank = [1]*(n+1)
def find(ind):
    if root[ind] < 0:
        return ind
    return find(root[ind])
def union(one, two):
    parentOne = find(one)
    parentTwo = find(two)
    if parentOne == parentTwo:
        return 0
    if rank[parentOne] > rank[parentTwo]:
        root[parentOne] += root[parentTwo]
        root[parentTwo] = parentOne
    elif rank[parentTwo] > rank[parentOne]:
        root[parentTwo] += root[parentOne]
        root[parentOne] = parentTwo
    else:
        root[parentOne] += root[parentTwo]
        root[parentTwo] = parentOne
        rank[parentOne] += 1
for i in range(q):
    query = input().split()
    if query[0] == "Q":
        print(-1*(root[find(int(query[1]))])) 
    else:
        union(int(query[1]), int(query[2]))