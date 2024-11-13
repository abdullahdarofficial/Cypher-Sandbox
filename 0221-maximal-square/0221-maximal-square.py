class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:  # Check for empty matrix
            return 0
    
        m, n = len(matrix), len(matrix[0])  # Get matrix dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # DP table to store side lengths
        max_side = 0  # Variable to track the maximum side length
    
        for i in range(1, m + 1):  # Start from 1 to handle boundary conditions
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':  # If the current cell is '1'
                    # Update dp[i][j] based on previous rows and columns
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])  # Update the maximum side length
    
        return max_side * max_side  # Return the area of the largest square
