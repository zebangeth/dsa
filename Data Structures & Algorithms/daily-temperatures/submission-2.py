class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, idx)
        result = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                pre_t, pre_i = stack.pop()
                result[pre_i] = idx - pre_i
            stack.append((t, idx))
        return result
