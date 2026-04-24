class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for i, num in enumerate(nums): 
            if target - num in visited: 
                return [visited[target - num], i]
            visited[num] = i
        return [-1, -1]