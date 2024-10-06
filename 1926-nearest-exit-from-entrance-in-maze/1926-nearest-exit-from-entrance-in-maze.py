class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        

   
        rows = len(maze)
        cols = len(maze[0])
        def checkExit(x, y):
            if (x == 0 or y == 0 or x == rows - 1 or y == cols - 1) and (x,y) != (entrance[0], entrance[1]):
                return True 
            return False 

        visited = set()
        queue = deque([(entrance[0], entrance[1], 0)])
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        allexits = []
        while queue:
            x, y, count = queue.popleft()

            if checkExit(x, y):
                return count

            if (x, y) in visited:
                continue

            visited.add((x,y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    queue.append((nx, ny, count + 1))
        print(allexits)
        if allexits:
            return min(allexits)
        return -1

            