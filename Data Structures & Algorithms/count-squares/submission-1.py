class CountSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)
        self.xs = collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xs[x].add(y)
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for py in self.xs[x]:
            if py == y:
                continue
            border = py - y
            res += self.points[(x + border, y)] * self.points[(x + border, py)] * self.points[(x, py)]
            res += self.points[(x - border, y)] * self.points[(x - border, py)] * self.points[(x, py)]
        
        return res
        
