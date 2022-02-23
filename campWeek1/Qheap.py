import heapq

dicts = {}
heap = []
n = eval(input())

while n>0:
    temp = input().split(' ')
    if temp[0]=='1':
        heapq.heappush(heap,int(temp[1]))    #since the space is counted as a character
        if temp[1] in dicts:
            dicts[int(temp[1])] += 1
        else:
            dicts[int(temp[1])] = 1          
    elif temp[0] == '2':
        dicts[int(temp[1])] -= 1
    elif temp[0] == '3': 
        while dicts[heap[0]] == 0:
            heapq.heappop(heap)    
        print(heap[0])
    n -= 1