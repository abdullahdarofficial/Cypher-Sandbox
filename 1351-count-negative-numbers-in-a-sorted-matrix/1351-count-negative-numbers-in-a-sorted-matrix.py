class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        negatives = 0
        for row in grid:
            low, high = 0, len(row) - 1

            while low <= high:
                mid = (low + high ) // 2
                if row[mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1

            negatives += len(row) - low
        return negatives

        

                