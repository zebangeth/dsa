class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state: dp[i] stores the min number of coins need to make up amount i
        dp = [float('inf')] * (amount + 1)

        # initialization:
        dp[0] = 0
        coins.sort()

        # state transition:
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i - coin] + 1, dp[i])

        # answer:
        return dp[amount] if dp[amount] != float('inf') else -1
