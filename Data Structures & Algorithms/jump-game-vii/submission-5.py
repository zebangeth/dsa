class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        # state: dp[i] stores if s[i] is reachable
        dp = [False] * len(s)

        # init
        dp[0] = True

        # state transition function
        for i in range(1, len(s)):
            for j in range(minJump, maxJump + 1):
                if s[i] == '1' or i - j < 0:
                    continue
                if dp[i - j]:
                    dp[i] = True
                    break
        
        return dp[len(s) - 1]
