from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = [0 for _ in range(numCourses)]

        # Step 1: Build the graph and indegree array
        for curr, p_req in prerequisites:
            if p_req not in graph:
                graph[p_req] = []
            graph[p_req].append(curr)
            indegree[curr] += 1

        # Step 2: Initialize the queue with courses having no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Process the queue
        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            # Decrease the indegree of neighbors
            for neighbor in graph.get(course, []):  # Use .get() to handle courses with no neighbors
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses have been processed
        return count == numCourses
