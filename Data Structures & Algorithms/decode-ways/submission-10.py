class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) < 1 or s[0] == '0':
            return 0

        decodables = [str(i) for i in range(1, 27)]

        # state: dp[i] stores the number of ways to decode s[:i]
        dp = [0] * (len(s) + 1)

        # initialization
        dp[0] = 1
        dp[1] = 1

        # state transition function
        for i in range(1, len(s)):
            cur = s[i]
            prv = s[i-1:i+1]
            if cur in decodables and prv in decodables:
                dp[i + 1] = dp[i] + dp[i - 1]
            elif cur in decodables:
                dp[i + 1] = dp[i]
            elif prv in decodables:
                dp[i + 1] = dp[i - 1]
            else:
                return 0

        print(dp)
        return dp[len(s)]


