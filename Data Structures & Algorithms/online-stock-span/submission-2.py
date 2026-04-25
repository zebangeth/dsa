class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0
        

    def next(self, price: int) -> int:
        self.day += 1
        cur_stock = (price, self.day)
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.stack.append(cur_stock)
        return self.day - self.stack[-2][1] if len(self.stack) > 1 else self.day

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)