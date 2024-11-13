class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        maxsize = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def pr():
            for row in dp:
                print(row)
            print()

        for i in range(m + 1):
            for j in range(n + 1):
                pr()
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxsize = max(maxsize, dp[i][j])
                
        return maxsize * maxsize

