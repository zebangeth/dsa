class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        self.dfs(nums, used, [], ans)
        return ans

    def dfs(self, nums, used, path, ans):
        if len(path) == len(nums):
            ans.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            used[i] = True
            path.append(nums[i])
            
            self.dfs(nums, used, path, ans)
            
            path.pop()
            used[i] = False