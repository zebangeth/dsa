class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])

        
        # state: dp[i][0] stores the max profit with no stock on the ith day
        dp = [[0] * 2 for _ in range(len(prices))]

        # initialization
        dp[0][1] = -prices[0]
        dp[1][1] = -min(prices[:2])
        dp[1][0] = max(prices[1] + dp[1][1], dp[0][0])

        # transition function: 
        for i in range(2, len(prices)):
            # if has stock: had stock and hold / no stock and buy today
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            # if no stock: had stock and sell / no stock and remain no stock
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
        
        print(dp)
        # answer
        return max(dp[len(prices) - 1])