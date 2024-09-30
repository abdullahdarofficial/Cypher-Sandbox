class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        # n = len(grid)
        # times = 0
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i] == [grid[k][j] for k in range(n)]:
        #             times += 1
        # return times

        n = len(grid)
        row_count = defaultdict(int)
        times = 0
        
        # Store the frequency of each row as a tuple
        for row in grid:
            row_count[tuple(row)] += 1
        
        # Check each column and see if it matches any row
        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            if column in row_count:
                times += row_count[column]
        
        return times