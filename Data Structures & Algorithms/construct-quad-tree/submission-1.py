"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.c_help(grid, 0, 0, len(grid), len(grid[0]))
    
    def c_help(self, grid, r_start, c_start, r_end, c_end):
        can_prune = True
        for r in range(r_start, r_end):
            for c in range(c_start, c_end):
                if grid[r][c] != grid[r_start][c_start]:
                    can_prune = False
                    break
        
        if can_prune:
            return Node(grid[r_start][c_start] == 1, True, None, None, None, None)
        
        mid_r = (r_start + r_end) // 2
        mid_c = (c_start + c_end) // 2
        return Node(
            val=True,
            isLeaf=False,
            topLeft=self.c_help(grid, r_start, c_start, mid_r, mid_c),
            topRight=self.c_help(grid, r_start, mid_c, mid_r, c_end),
            bottomLeft=self.c_help(grid, mid_r, c_start, r_end, mid_c),
            bottomRight=self.c_help(grid, mid_r, mid_c, r_end, c_end),
        )
