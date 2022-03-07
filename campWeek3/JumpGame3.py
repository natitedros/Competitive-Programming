class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        visited = set()
        q.append(start)
        visited.add(start)
        n = len(arr)
        while q:
            ind = q.popleft()
            if arr[ind] == 0:
                return True
            if ind + arr[ind] < n and (ind+arr[ind]) not in visited:
                q.append(ind+arr[ind])
                visited.add(ind+arr[ind])
            if ind - arr[ind] >= 0 and (ind-arr[ind]) not in visited:
                q.append(ind-arr[ind])
                visited.add(ind-arr[ind])
        return False