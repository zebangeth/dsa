class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque() # num, idx
        result = []
        for i in range(len(nums)):
            while queue and queue[-1][0] < nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            if queue[0][1] < i + 1 - k:
                queue.popleft()
            if i + 1 >= k:
                result.append(queue[0][0])
        return result
            
