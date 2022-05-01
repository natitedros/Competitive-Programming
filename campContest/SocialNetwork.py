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

people, edges = invr()
root = [0]*(people+1)
rank = [1]*(people+1)
size = {}
for i in range(people+1):
    root[i] = i
    size[i] = 1
def find(person):
    if root[person] == person:
        return person
    return find(root[person])
def union(one, two):
    parentOne = find(one)
    parentTwo = find(two)
    if parentOne == parentTwo:
        return 0
    if rank[parentOne] > rank[parentTwo]:
        root[parentTwo] = parentOne
        size[parentOne] += size[parentTwo]
    elif rank[parentTwo] > rank[parentOne]:
        root[parentOne] = parentTwo
        size[parentTwo] += size[parentOne]
    else:
        root[parentTwo] = parentOne
        rank[parentOne] += 1
        size[parentOne] += size[parentTwo]
maxSize = 0
for i in range(edges):
    p1, p2 = invr()
    union(p1, p2)
    temp = size[find(p1)]-1
    if temp > maxSize:
        maxSize = temp
    print(maxSize)