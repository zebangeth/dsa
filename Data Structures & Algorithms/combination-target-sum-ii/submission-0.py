class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.dfs(candidates, target, 0, [])
        return self.ans

    def dfs(self, candidates, target, i, combination):
        if target == 0:
            self.ans.append(combination[:])
            return
        
        if target < 0 or i >= len(candidates):
            return
        
        # 选 candidates[i]
        combination.append(candidates[i])
        self.dfs(candidates, target - candidates[i], i + 1, combination)
        combination.pop()

        # 不选 candidates[i]：跳过后面所有相同的 candidates[i]
        while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
            i += 1
        
        self.dfs(candidates, target, i + 1, combination)