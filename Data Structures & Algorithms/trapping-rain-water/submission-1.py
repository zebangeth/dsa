class Solution:
    def trap(self, height: List[int]) -> int:
        max_before = [0] * len(height)
        max_after = [0] * len(height)
        for i in range(len(height)):
            if i == 0 or max_before[i - 1] < height[i]:
                max_before[i] = (height[i])
                continue
            max_before[i] = max_before[i - 1]
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1 or max_after[i + 1] < height[i]:
                max_after[i] = (height[i])
                continue
            max_after[i] = max_after[i + 1]

        water = 0
        waters = []
        for i in range(1, len(height) - 1):
            water += max(0, min(max_before[i - 1], max_after[i + 1]) - height[i])
        return water

# [0,2,0,3,1,0,1,3,2,1]
#  0 2 2 3 3 3 3 3 3 3
#  3 3 3 3 3 3 3 3 2 1
#    0 2 0 2 