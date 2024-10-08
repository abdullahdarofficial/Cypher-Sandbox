class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    queue.append((i,j))


        if count == 0:
            return 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        levels = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        count -= 1
            levels += 1

        return levels - 1 if count == 0 else -1