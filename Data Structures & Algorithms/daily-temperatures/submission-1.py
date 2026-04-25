class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            # if not stack:
            #     stack.append((i, t))
            # else:
            while stack and stack[-1][1] < t:
                prev_i, prev_t = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((i, t))

        return result
                
