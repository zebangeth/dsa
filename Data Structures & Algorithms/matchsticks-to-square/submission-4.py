class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        side = total // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > side:
            return False

        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side

            stick = matchsticks[i]

            for j in range(4):
                if sides[j] + stick > side:
                    continue

                sides[j] += stick

                if dfs(i + 1):
                    return True

                sides[j] -= stick

                # 剪枝：如果这个 stick 放进一个空边失败了，
                # 那么放进其他空边也是等价的，不需要再试
                if sides[j] == 0:
                    break

            return False

        return dfs(0)