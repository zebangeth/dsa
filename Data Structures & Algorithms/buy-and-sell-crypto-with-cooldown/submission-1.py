class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # state: dp[i][0/1] stores the max profit wo/w stock on the ith day
        dp = [[0] * 2 for _ in range(len(prices))]

        # init
        dp[0][0], dp[0][1] = 0, -prices[0]

        # state transition function
        for i in range(1, len(prices)):
            # no stock: (no stock prev day, sell stock today)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

            # has stock: (has stock prev day, buy stock today)
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        
        print(dp)
        return max(dp[len(prices) - 1])