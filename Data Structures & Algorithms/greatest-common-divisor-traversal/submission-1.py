class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        factor_to_index = {}

        for i, x in enumerate(nums):
            d = 2
            while d * d <= x:
                if x % d == 0:
                    if d in factor_to_index:
                        union(i, factor_to_index[d])
                    else:
                        factor_to_index[d] = i

                    while x % d == 0:
                        x //= d
                d += 1

            # 剩下的大于 1 的 x 本身也是一个质因子
            if x > 1:
                if x in factor_to_index:
                    union(i, factor_to_index[x])
                else:
                    factor_to_index[x] = i

        root = find(0)
        return all(find(i) == root for i in range(n))