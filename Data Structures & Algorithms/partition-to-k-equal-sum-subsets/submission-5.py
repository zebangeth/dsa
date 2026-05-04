class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if len(nums) < k or total % k != 0:
            return False
        
        bucket_size = total // k

        nums.sort(reverse=True)

        if nums[0] > bucket_size:
            return False
        
        buckets = [0] * k
        memo = {}

        return self.dfs(nums, 0, buckets, bucket_size, memo)
        
    def dfs(self, nums, i, buckets, bucket_size, memo):
        key = (i, tuple(sorted(buckets)))

        if key in memo:
            return False

        if i == len(nums):
            return all(b == bucket_size for b in buckets)
        
        seen = set()

        for j in range(len(buckets)):
            if buckets[j] in seen:
                continue
            seen.add(buckets[j])

            if buckets[j] + nums[i] > bucket_size:
                continue

            buckets[j] += nums[i]

            if self.dfs(nums, i + 1, buckets, bucket_size, memo):
                return True

            buckets[j] -= nums[i]

            # 如果放进一个空 bucket 都失败了，
            # 放进其他空 bucket 也是等价的
            if buckets[j] == 0:
                break

        memo[key] = False
        return False