class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][w] stores the number of ways to get amount w with coins[:i]
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # initialization
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        # function
        for i in range(1, len(coins) + 1):
            for w in range(amount + 1):
                if coins[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                    continue
                # take coins[i - 1] or not
                dp[i][w] = dp[i - 1][w] + dp[i][w - coins[i - 1]]
        # answer
        return dp[len(coins)][amount]