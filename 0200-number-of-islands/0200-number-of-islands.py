class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        def recursive(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
                grid[i][j] = "2"
                recursive(i + 1, j)
                recursive(i - 1, j)
                recursive(i, j + 1)
                recursive(i, j - 1)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    recursive(i,j)
                    count += 1

        return count