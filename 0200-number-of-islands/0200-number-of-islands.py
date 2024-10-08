class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        num_islands = 0

        def bfs(i: int, j: int):

            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            queue = deque([(i,j)])
            visited[i][j] = True

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '1':
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    num_islands += 1

        return num_islands