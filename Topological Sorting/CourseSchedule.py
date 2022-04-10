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