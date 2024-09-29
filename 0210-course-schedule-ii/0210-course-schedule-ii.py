class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        indegree = [0 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        
        courses = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            course = queue.popleft()
            courses.append(course)
            count += 1

            for neighbor in graph.get(course, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return courses if numCourses == count else []