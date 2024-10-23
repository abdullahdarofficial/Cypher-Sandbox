class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        
        # n = len(grid)
        # m = len(grid[0])
    
        # maxcount = 0
        # for i in range(n):
        #     for j in range(m):

        #         if grid[i][j] == 1: # somethong found now up down right left

        #             for k in range(j+1, m): # go right
        #                 if grid[i][k] == 1:
        #                     for l in range(i + 1, n): # go up
        #                         if grid[l][j] == 1:
        #                             maxcount += 1
        #                     for l in range(i - 1, -1, -1): # go down
        #                         if grid[l][j] == 1:
        #                             maxcount += 1
        #             for k in range(j-1,-1,-1): # go left
        #                 if grid[i][k] == 1:
        #                     for l in range(i + 1, n): # go up
        #                         if grid[l][j] == 1:
        #                             maxcount += 1
        #                     for l in range(i - 1, -1, -1): # go down
        #                         if grid[l][j] == 1:
        #                             maxcount += 1
                            
        # return maxcount

        if not grid or not grid[0]:  # Handle empty grid case
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        maxcount = 0

        # Iterate over every cell in the grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # Found a `1`
                    # Count right in the row
                    right_count = sum(grid[i][k] for k in range(j + 1, m))  # Count 1s to the right
                    left_count = sum(grid[i][k] for k in range(j))  # Count 1s to the left
                    down_count = sum(grid[k][j] for k in range(i + 1, n))  # Count 1s below
                    up_count = sum(grid[k][j] for k in range(i))  # Count 1s above

                    # Calculate possible triangles
                    maxcount += right_count * up_count  # Right triangle formed
                    maxcount += right_count * down_count  # Right triangle formed
                    maxcount += left_count * up_count  # Left triangle formed
                    maxcount += left_count * down_count  # Left triangle formed
        
        return maxcount