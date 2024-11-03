class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        
        # size = len(b)
        # maxscore = float('-inf')
        # for i in range(size - 3):
        #     for j in range(i + 1, size - 2):
        #         for k in range(j + 1, size - 1):
        #             for l in range(k + 1, size):
        #                 # here we get all combinations
        #                 maxscore = max(maxscore, a[0] * b[i] + a[1] * b[j] + a[2] * b[k] + a[3] * b[l])
        # return maxscore

        # with DP

        m = len(a)
        n = len(b)
        
        # Create a DP table initialized to negative infinity
        dp = [[-float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: when no elements are chosen from `a` or `b`
        for j in range(n + 1):
            dp[0][j] = 0  # If we choose 0 from a, score is 0
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(i, n + 1):  # Start from i to ensure j >= i
                # Option 1: Skip current b[j - 1]
                dp[i][j] = dp[i][j - 1]
                # Option 2: Include current a[i - 1] * b[j - 1]
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + a[i - 1] * b[j - 1])
        
        # The answer is the maximum score we can get using all elements in `a` and `b`
        return dp[m][n]