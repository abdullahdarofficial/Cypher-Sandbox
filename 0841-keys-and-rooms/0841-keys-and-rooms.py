class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {}
        for index, room in enumerate(rooms):
            graph[index] = room

        stack = []
        stack.append(0)
        self.count = 0
        def dfs(stack, visited):
            if not stack:
                return

            roomno = stack.pop()
            if roomno not in visited:
                visited.add(roomno)
                self.count += 1
                for neighbor in graph[roomno]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        dfs(stack, visited)
        dfs([0], set())
        return self.count == len(rooms)

        





