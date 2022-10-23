class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employees = defaultdict(list)
        for employee in range(n):
            if employee == headID:
                continue
            employees[manager[employee]].append(employee)
        queue = deque()
        queue.append((headID,0))
        
        time = 0
        while queue:
            length = len(queue)
            while length:
                length -= 1
                person, tellTime = queue.popleft()
                time = max(time, tellTime)
                for listener in employees[person]:
                    queue.append((listener, informTime[person]+tellTime))

        return time
            