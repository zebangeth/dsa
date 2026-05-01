class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        self.dfs(n, k, 1, [])
        return self.combinations
    
    def dfs(self, n, k, start, combination):
        if k == 0:
            self.combinations.append(combination[:])
            return
        
        for i in range(start, n + 1):
            self.dfs(n, k - 1, i + 1, combination + [i])