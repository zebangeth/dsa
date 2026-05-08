class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        # state: dp[i][j] stores if s[i:j+1] is a palindrome
        dp = [[0] * len(s) for _ in range(len(s))]

        result = 0
        # initialization
        for i in range(len(s)):
            dp[i][i] = 1
            result += 1
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                result += 1
        
        # function
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = 1
                    result += 1
        
        return result