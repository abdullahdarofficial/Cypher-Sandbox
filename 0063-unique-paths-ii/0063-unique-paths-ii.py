class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # # recursion

        # n = len(obstacleGrid)
        # m = len(obstacleGrid[0])
        # def recursion(i,j):
        #     if 0 <= i < n and 0 <= j < m and obstacleGrid[i][j] == 0:
        #         if i == n-1 and j == m-1:
        #             return 1
        #         else:
        #             return recursion(i + 1, j) + recursion(i, j + 1)
        #     else:
        #         return 0
        # return recursion(0,0)


        # dp

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1:
            return 0

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] == 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        return dp[n-1][m-1]