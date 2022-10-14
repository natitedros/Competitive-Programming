# BFS Approach
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incomming = [0]*numCourses
        outgoing = defaultdict(set)
        for course, pre in prerequisites:
            incomming[course] += 1
            outgoing[pre].add(course)
        queue = deque()
        res = []
        for course in range(numCourses):
            if incomming[course] == 0:
                queue.append(course)
                res.append(course)
        count = 0
        while queue:
            course = queue.popleft()
            for dependent in outgoing[course]:
                incomming[dependent] -= 1
                if incomming[dependent] == 0:
                    queue.append(dependent)
                    res.append(dependent)
            count += 1
        if count == numCourses:
            return res
        return []

# DFS Approach
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outgoing = defaultdict(list)
        for course,pre in prerequisites:
            outgoing[pre].append(course)
        stk = []
        color = [0]*numCourses
        def dfs(course):
            if color[course] == 1:
                return False
            if color[course] == 2:
                return True
            color[course] = 1
            for post in outgoing[course]:
                if not dfs(post):
                    return False
            color[course] = 2
            stk.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return stk[::-1]