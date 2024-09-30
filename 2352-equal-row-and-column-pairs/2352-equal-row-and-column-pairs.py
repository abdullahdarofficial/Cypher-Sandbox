class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        times = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == [grid[k][j] for k in range(n)]:
                    times += 1
        return times
