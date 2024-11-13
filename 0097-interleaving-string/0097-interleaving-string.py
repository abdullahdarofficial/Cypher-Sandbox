class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n = len(s1)
        m = len(s2)
        o = len(s3)

        if n + m != o:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp [0][0] = True
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i < n and dp[i][j] and s1[i] == s3[i+j]:
                    dp[i+1][j] = True
                if j < m and dp[i][j] and s2[j] == s3[i+j]:
                    dp[i][j+1] = True

        return dp[n][m]
