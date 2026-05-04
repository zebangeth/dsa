class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        
        border = total_len // 4
        if max(matchsticks) > border:
            return False
        
        return self.dfs(matchsticks, border, set(), 0, 0)
    
    def dfs(self, matchsticks, border, visited, good_piles, current_pile):
        if len(visited) == len(matchsticks) and good_piles == 4:
            return True
        
        for i in range(len(matchsticks)):
            if i in visited:
                continue
            if matchsticks[i] + current_pile > border:
                continue
            elif matchsticks[i] + current_pile == border:
                if self.dfs(matchsticks, border, visited | set([i]), good_piles + 1, 0):
                    return True
            else:
                if self.dfs(matchsticks, border, visited | set([i]), good_piles, matchsticks[i] + current_pile):
                    return True

        return False
