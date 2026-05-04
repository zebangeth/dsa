class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or sum(nums) % k != 0:
            return False
        
        buckets = [0] * k
        bucket_size = sum(nums) // k
        nums.sort(reverse=True)
        if nums[0] > bucket_size:
            return False
        return self.dfs(nums, 0, buckets, bucket_size, dict())
        
    def dfs(self, nums, i, buckets, bucket_size, memo):
        key = (i, tuple(sorted(buckets)))
        if key in memo:
            return False

        if i == len(nums):
            return True
        
        for j in range(len(buckets)):
            if buckets[j] + nums[i] > bucket_size:
                continue
            buckets[j] += nums[i]
            if self.dfs(nums, i + 1, buckets, bucket_size, memo):
                return True
            buckets[j] -= nums[i]
        
        memo[key] = False
        return False
