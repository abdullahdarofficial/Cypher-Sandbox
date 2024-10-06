class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # count = 0
        # for connection in connections:
        #     if connection[0] < connection[1]:
        #         connection[0], connection[1] = connection[1], connection[0]
        #         count += 1

        # return count

        
            
        
        # if not connections:
        #     return None

        # count = 0
        # correct = set()
        # correct.add(0)

        # connections.sort(key=lambda x: x[1])

        # for connect in connections:
        #     first, second = connect
        #     if second in correct:
        #         correct.add(first)
        #     else:
        #         count += 1
        #         correct.add(second)

        # return count

        graph = {}

        for a, b in connections:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, 1))
            graph[b].append((a, 0))


        queue = deque([0])
        visited = set([0])
        count = 0

        while queue:
            city = queue.popleft()
            for neighbor, needs_reorder in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    count += needs_reorder

        return count




