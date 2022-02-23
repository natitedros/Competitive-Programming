def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    counter = 0
    while len(A)>=2 and A[0] < k:
        counter += 1
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        temp = first + 2*second
        heapq.heappush(A, temp)
        
    if A[0] >= k:
        return counter
    return -1