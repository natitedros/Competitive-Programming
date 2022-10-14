#BFS Approach

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neededPre = [0]*numCourses
        outgoing = defaultdict(set)
        for course,pre in prerequisites:
            neededPre[course] += 1
            outgoing[pre].add(course)
        queue = deque()
        for course in range(numCourses):
            if neededPre[course] == 0:
                queue.append(course)
        count = 0
        while queue:
            course = queue.popleft()
            for dependents in outgoing[course]:
                neededPre[dependents] -= 1
                if neededPre[dependents] == 0:
                    queue.append(dependents)
            count += 1
        return count==numCourses

# DFS Approach
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
                return False
        return True
                