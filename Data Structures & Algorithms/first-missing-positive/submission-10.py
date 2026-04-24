class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Solution 1: using a set to store unique values
        # and then check if num exist starting from 1
        # O(n), O(n)
        # ---
        # unique = set(nums)
        # min_num = 1
        # while min_num in unique:
        #     min_num += 1
        # return min_num

        # Solution 2: using the nums array as the hashset
        # nums[idx] can represent if num=idx in nums
        # how to store? by the sign of nums[idx]
        # what if the sign of nums[idx] is neg in the original array?
        # replace neg num by 0 as they are useless anyway
        # O(n), O(n)
        # for i, num in enumerate(nums):
        #     if num < 0:
        #         nums[i] = 0

        # for num in nums:
        #     num = abs(num)
        #     if 0 < num <= len(nums):
        #         if nums[num - 1] == 0:
        #             nums[num - 1] = -1
        #         nums[num - 1] = -abs(nums[num - 1])
        
        # i = 1
        # print(nums)
        # while i <= len(nums) and nums[i - 1] < 0:
        #     i += 1
        # return i

        # Solution 3: Cycle Sort
        n = len(nums)
        i = 0

        # 第一阶段：把每个值 x 尽量放到下标 x - 1 的位置上
        # 例如 1 放到 nums[0]，2 放到 nums[1]，3 放到 nums[2]
        while i < n:
            correct = nums[i] - 1

            # 只有当 nums[i] 是 [1, n] 范围内的有效正整数时，
            # 它才有资格被放到“正确位置”
            # 同时 nums[i] != nums[correct] 用来避免重复值导致死循环
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                # 把当前值交换到它应该去的位置
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                # 以下情况直接跳过：
                # 1. nums[i] <= 0
                # 2. nums[i] > n
                # 3. nums[i] 已经在正确位置
                # 4. 目标位置上已经有相同的值（重复元素）
                i += 1

        # 第二阶段：从左到右检查
        # 第一个 nums[i] != i + 1 的位置，说明 i + 1 缺失
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果 1 到 n 都在正确位置上，答案就是 n + 1
        return n + 1


