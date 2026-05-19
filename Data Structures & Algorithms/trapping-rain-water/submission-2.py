class Solution:
    def trap(self, height: List[int]) -> int:
        high_before = [0] * len(height)
        high_after = [0] * len(height)
        for i in range(1, len(height)):
            high_before[i] = max(high_before[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            high_after[i] = max(high_after[i + 1], height[i + 1])
        
        water = 0
        for i in range(1, len(height) - 1):
            water += max(0, min(high_after[i], high_before[i]) - height[i])
        return water


        