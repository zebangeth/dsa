class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # state: dp[i][j] stores is s[:i] matches p[:j]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # initialization
        dp[0][0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # function
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j - 1] == '*':
                    # c* matches zero chars in s
                    dp[i][j] = dp[i][j] or dp[i][j - 2]
                    # 
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        print(dp)
        # answer
        return dp[len(s)][len(p)]