class Solution:
    def checkValidString(self, s: str) -> bool:
        # 最少/多可能还剩多少个 open left parenthesis(未匹配的 '(')
        l_min, l_max = 0, 0
        for c in s:
            if c == '(':
                l_min, l_max = l_min + 1, l_max + 1
            elif c == ')':
                l_min, l_max = l_min - 1, l_max - 1
            else:
                l_min -= 1 # 把 * 当成 )
                l_max += 1 # 把 * 当成 (

            if l_max < 0:
                return False
            l_min = max(l_min, 0)

        
        return l_min == 0
