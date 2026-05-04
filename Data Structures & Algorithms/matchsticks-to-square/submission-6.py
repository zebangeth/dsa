class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False

        req_side = total_len // 4
        sorted_matchs = sorted(matchsticks, reverse=True)
        if sorted_matchs[0] > req_side:
            return False

        # initialize 4 buckets, one for each side to collect matchsticks
        sides = [0] * 4
        memo = dict()
        return self.dfs(sorted_matchs, sides, req_side, 0, memo)

    def dfs(self, matchs, sides, req_side, i, memo):
        # Memoization key is the tuple of sorted sides + current index i
        key = (i, tuple(sorted(sides)))
        if key in memo:
            return memo[key]
        
        # If all matchsticks are used, and no sides > req_side, return True
        if i == len(matchs):
            return True

        seen = set()
        # can put the current match[i] on one of the 4 sides
        for j in range(4):
            # 如果两个 side 当前长度一样，把 stick 放进去的效果等价
            if sides[j] in seen:
                continue
            seen.add(sides[j])
            if sides[j] + matchs[i] <= req_side:
                sides[j] += matchs[i]
                if self.dfs(matchs, sides, req_side, i + 1, memo):
                    return True
                sides[j] -= matchs[i]
            # 如果放进一个空 side 都失败了，其他空 side 也不用试
            if sides[j] == 0:
                break

        memo[key] = False
        return False
