class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] stores if word[:i] is breakable
        dp = [False] * (len(s) + 1)

        # initialization
        dp[0] = True

        # function
        for i in range(len(s) + 1):
            for word in wordDict:
                if len(word) > i or not dp[i - len(word)]:
                    continue
                dp[i] = dp[i] or word == s[i - len(word) : i]

        return dp[-1]
