class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case for very small n values
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # DP array to store results of subproblems
        dp = [[0] * 3 for _ in range(n + 1)]
        
        # Base cases
        dp[1][0] = 1
        dp[2][0] = 2
        dp[2][1] = 1
        dp[2][2] = 1

        # Fill the dp array for all values from 3 to n
        for i in range(3, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 2][0] + dp[i - 1][1]) % MOD
        
        return dp[n][0]
