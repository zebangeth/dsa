class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 2 and (v := max(nums)) == min(nums):
            return (
                ((n-2)*(v*v*v))+(v*v)+v
            )
        cache = {}
        nums = [1] + nums + [1]
        n = len(nums)
        def dfs(l, r): # in this interval, which one is the last to pop
            nonlocal n
            if l + 1 == r:
                # no middle balloons to pop, return
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            res = 0
            for i in range(l+1, r):
                score = nums[l]*nums[i]*nums[r]
                score += dfs(l, i) + dfs(i, r)
                res = max(res, score)
            cache[(l, r)] = res
            return res
        return dfs(0, n-1)


