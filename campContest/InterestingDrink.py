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

shops = inp()
priceList = inlt()
days = inp()
budget = []
for i in range(days):
    budget.append(inp())
priceList.sort()

for i in range(days):
    left = 0
    right = shops-1
    count =0
    while left <= right:
        mid = left + (right-left)//2
        if priceList[mid] <= budget[i]:
            left = mid+1
            count = mid +1

        elif priceList[mid] > budget[i]:
            right = mid-1
        # else:
        #     left = right = mid
        #     break
    print(count)
    # if left< days and priceList[left] <= budget[i]:
    #     print(left+1)
    # else: 
    #     print(left)






