class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a dp array with size amount + 1 (0 to amount)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # No coins are needed to make amount 0

        # Iterate over each amount from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:  # Check if we can use this coin
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, return -1 (meaning it's not possible)
        return dp[amount] if dp[amount] != float('inf') else -1
