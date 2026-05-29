class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        # state: dp[i] stores if s[i] is reachable
        dp = [False] * len(s)

        # init
        dp[0] = True
        count = 0

        # state transition function
        for i in range(1, len(s)):
            if i - minJump >= 0 and dp[i - minJump]:
                count += 1
            if i - maxJump > 0 and dp[i - maxJump - 1]:
                count -= 1
            if count >= 1 and s[i] == '0':
                dp[i] = True

        return dp[len(s) - 1]
