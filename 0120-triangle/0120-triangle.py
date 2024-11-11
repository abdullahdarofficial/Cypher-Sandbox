class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # # greedy approach
        # idx = 0
        # curr = triangle[0][idx]
        # for i in range(1, len(triangle)):
        #     if triangle[i][idx] < triangle[i][idx + 1]:
        #         curr += triangle[i][idx]
        #     else:
        #         curr += triangle[i][idx + 1]
        #         idx += 1
        # return curr

        # dp

        dp = triangle[-1]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]