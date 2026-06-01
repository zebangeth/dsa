class FreqStack:

    def __init__(self):
        self.frq_to_nums = collections.defaultdict(list)
        self.nums_to_frq = collections.defaultdict(int)
        self.max_frq = 0
        

    def push(self, val: int) -> None:
        self.nums_to_frq[val] += 1
        frq = self.nums_to_frq[val]
        self.max_frq = max(self.max_frq, frq)
        self.frq_to_nums[frq].append(val)
        

    def pop(self) -> int:
        if not self.frq_to_nums[self.max_frq]:
            del self.frq_to_nums[self.max_frq]
            self.max_frq -= 1
        popped = self.frq_to_nums[self.max_frq].pop()
        self.nums_to_frq[popped] -= 1
        return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()