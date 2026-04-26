class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # (idx, num)
        queue = collections.deque()
        result = []
        for i in range(len(nums)):
            if queue and i - queue[0][0] >= k:
                queue.popleft()
            while queue and queue[-1][1] <= nums[i]:
                queue.pop()
            queue.append((i, nums[i]))
            if i + 1 >= k:
                result.append(queue[0][1])
        return result
