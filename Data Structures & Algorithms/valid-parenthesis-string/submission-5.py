class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = dict()
        return self.dfs(s, 0, 0, 0, memo)
        
    def dfs(self, s, i, l_open, r_open, memo):
        if (i, l_open, r_open) in memo:
            return memo[(i, l_open, r_open)]

        if r_open > l_open:
            return False

        if i == len(s):
            if l_open == r_open:
                return True
            return False
        
        is_valid = False
        if s[i] == '(':
            is_valid = self.dfs(s, i + 1, l_open + 1, r_open, memo)
        elif s[i] == ')':
            is_valid = self.dfs(s, i + 1, l_open, r_open + 1, memo)
        elif s[i] == '*':
            treated_as_l = self.dfs(s, i + 1, l_open + 1, r_open, memo)
            treated_as_r = self.dfs(s, i + 1, l_open, r_open + 1, memo)
            treated_as_empty = self.dfs(s, i + 1, l_open, r_open, memo)
            is_valid = treated_as_l or treated_as_r or treated_as_empty
        else:
            raise ValueError("input contains invalid chars")

        memo[(i, l_open, r_open)] = is_valid
        return is_valid

