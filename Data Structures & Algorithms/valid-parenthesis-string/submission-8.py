class Solution:
    def checkValidString(self, s: str) -> bool:
        # 最少/多可能还剩多少个 open left parenthesis(未匹配的 '(')
        l_min, l_max = 0, 0
        for c in s:
            if c == '(':
                l_min, l_max = l_min + 1, l_max + 1
            elif c == ')':
                l_min, l_max = l_min - 1, l_max - 1
            elif c == '*':
                l_min = max(0, l_min - 1)
                l_max = l_max + 1
            else:
                raise ValueError("input contains invalid chars")
            if l_max < 0:
                return False        
        return l_min <= 0 <= l_max
